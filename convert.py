from pdf2image import convert_from_path
import os

def pdf_to_jpg_by_page(pdf_path, output_folder="output_images"):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    try:
        images = convert_from_path(pdf_path, dpi=100)

        for i, image in enumerate(images):
            # 导出为JPG格式，文件名格式为 "页码.jpg" (页码从1开始)
            page_num = i + 1
            output_filename = os.path.join(output_folder, f"{page_num}.jpg")
            image.save(output_filename, 'JPEG')
            print(f"已将第 {page_num} 页保存为 {output_filename}")

    except Exception as e:
        print(f"处理PDF文件时发生错误: {e}")

if __name__ == "__main__":
    input_pdf_file = '/Users/legendstane/Desktop/Lottery/pictures.pdf'

    output_directory = 'pages'

    pdf_to_jpg_by_page(input_pdf_file, output_directory)