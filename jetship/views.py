# views.py
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Post, Category, Subcategory, Guest
from .serializers import PostSerializer
from django.core.files.storage import default_storage
import uuid
from django.utils.text import slugify
from django.utils import timezone
from gotilo.settings import CLOUDFLARE_R2_BUCKET_ENDPOINT,CLOUDFLARE_R2_BUCKET



# Base URL for Cloudflare R2 (replace with your actual Cloudflare R2 base URL)
CLOUDFLARE_BASE_URL = f"${CLOUDFLARE_R2_BUCKET_ENDPOINT}/{CLOUDFLARE_R2_BUCKET}/media/"

class PostPagination(PageNumberPagination):
    page_size = 10  # Number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 50

class PostListAPIView(generics.ListAPIView):
    queryset = queryset = Post.objects.select_related('user', 'category', 'subcategory').all().order_by('-created_at') # Latest posts first
    serializer_class = PostSerializer
    pagination_class = PostPagination


@api_view(['POST'])
def posts(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        price_category = request.POST.get('price_category')
        phone_no = request.POST.get('phone_no')
        whatsapp_no = request.POST.get('whatsapp_no')
        state = request.POST.get('state')
        district = request.POST.get('district')
        taluka = request.POST.get('taluka')
        village = request.POST.get('village')
        images = request.FILES.getlist('images')  
        userphoneno = request.POST.get('userphoneno')
        category_link = request.POST.get('category')
        subcategory_link = request.POST.get('subcategory')

        # 1 User Mapping using Phone Number
        try:
            user = Guest.objects.get(phone_number=userphoneno)
        except Guest.DoesNotExist:
            return Response({'error': 'User with this phone number does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 2 Category & Subcategory Mapping
        try:
            category = Category.objects.get(category_link=category_link)
            subcategory = Subcategory.objects.get(subcategory_link=subcategory_link)  
        except (Category.DoesNotExist, Subcategory.DoesNotExist):
            return Response({'error': 'Invalid Category or Subcategory.'}, status=status.HTTP_400_BAD_REQUEST)

        # 3️ Image Upload Handling (Cloudflare R2 - uploads folder)
        image_urls = {}
        for index, image in enumerate(images):
            original_filename = image.name
            # print(original_filename)
            sanitized_filename = slugify(original_filename)  # Sanitize the filename
            unique_filename = f"uploads/2025/{uuid.uuid4()}_{sanitized_filename}.png"  # No leading slash
            # print(unique_filename)

            # Save image to Cloudflare R2 (using default storage system configured for Cloudflare)
            file_path = default_storage.save(unique_filename, image)
            # print("file path: " + file_path)

            # Generate full Cloudflare image URL
            full_image_url = f"{CLOUDFLARE_BASE_URL}{file_path}"
            # print(full_image_url)
            image_urls[f"image{index + 1}"] = full_image_url
        
        # print(image_urls)
        # 4 Final Post Creation
        post = Post.objects.create(
            user=user,
            category=category,
            subcategory=subcategory,
            title=title,
            description=description,
            price=price,
            price_category=price_category,
            phone_no=phone_no,
            whatsapp_no=whatsapp_no,
            state=state,
            district=district,
            taluka=taluka,
            village=village,
            images=image_urls,
            created_at=timezone.now()  
        )
        post.save()

        return Response({'message': 'Post created successfully.'}, status=status.HTTP_201_CREATED)
    
    else:
        return Response({'message': "invalid request"}, status=status.HTTP_400_BAD_REQUEST)

        


