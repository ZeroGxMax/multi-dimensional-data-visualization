# Phân tích và Thông tin chi tiết từ Dữ liệu & Biểu đồ

Dựa trên các biểu đồ được tạo ra từ các tập dữ liệu về khí hậu và thời tiết, dưới đây là những đánh giá và thông tin chi tiết (insight) chính:

## 1. Biểu đồ Nhiệt độ Trung bình Hàng tháng (Weather Heatmap)
- **Nội dung:** Biểu đồ thể hiện nhiệt độ trung bình hàng tháng của các thành phố (dữ liệu tại New Zealand giai đoạn 2016-2017).
- **Thông tin chi tiết:** Biểu đồ làm nổi bật tính thời vụ và sự chênh lệch nhiệt độ giữa các khu vực. Các dải màu ấm (đỏ) tập trung vào các tháng mùa hè (tháng 12 đến tháng 2 ở Nam Bán Cầu), trong khi màu lạnh (xanh dương) rơi vào các tháng mùa đông (tháng 6 đến tháng 8). So sánh giữa các dòng (các thành phố) giúp nhận biết thành phố nào có khí hậu ôn hòa hoặc khắc nghiệt hơn.

## 2. Mối quan hệ giữa Nhiệt độ, Độ ẩm và Lượng mưa (Weather Scatter Plot)
- **Nội dung:** Biểu đồ phân tán kết hợp nhiều chiều dữ liệu: độ ẩm (trục x), nhiệt độ (trục y), lượng mưa (kích thước điểm) và phân loại thành phố (màu sắc).
- **Thông tin chi tiết:** 
  - Cho thấy đặc trưng vi khí hậu của từng thành phố thông qua việc phân cụm màu sắc.
  - Quan sát sự tương quan giữa nhiệt độ và độ ẩm: sự phân bố của các điểm giúp nhận diện các điều kiện thời tiết phổ biến (ví dụ: lạnh và khô, hoặc nóng và ẩm).
  - Dựa vào kích thước điểm, có thể thấy lượng mưa lớn (điểm to) thường xuất hiện ở những điều kiện nhiệt độ và độ ẩm nào, từ đó dự đoán được mô hình thời tiết dễ gây mưa nhất tại các thành phố này.

## 3. Dị thường Nhiệt độ Toàn cầu (Global Temp Heatmap)
- **Nội dung:** Biểu đồ nhiệt hiển thị độ lệch nhiệt độ (anomalies) toàn cầu theo từng tháng, kéo dài từ năm 1880 đến năm 2025 (so sánh với trung bình giai đoạn 1951-1980).
- **Thông tin chi tiết:** Đây là minh chứng trực quan mạnh mẽ về **biến đổi khí hậu và sự nóng lên toàn cầu**.
  - Phần nửa trên của biểu đồ (những năm xa xưa) chủ yếu bao phủ bởi màu xanh dương, cho thấy nhiệt độ lúc đó thấp hơn mức chuẩn.
  - Càng dịch chuyển xuống dưới (những năm gần đây, đặc biệt từ cuối thế kỷ 20 và thế kỷ 21), dải màu chuyển dần sang đỏ và đỏ đậm. Điều này phản ánh rõ ràng nhiệt độ Trái Đất đang tăng lên một cách liên tục và đáng báo động.

## 4. Xu hướng Lượng mưa tại Minnesota (Minnesota Precip Line Chart)
- **Nội dung:** Biểu đồ đường thể hiện lượng mưa hàng tháng qua các năm (1927–1936) tại 6 trạm nông nghiệp ở tiểu bang Minnesota.
- **Thông tin chi tiết:** 
  - **Tính chu kỳ:** Các đường gấp khúc lên xuống liên tục cho thấy lượng mưa thay đổi mạnh mẽ theo mùa, với các tháng mưa nhiều và các tháng khô hạn lặp lại hàng năm.
  - **Biến động lịch sử:** Giai đoạn 1927-1936 là một thập kỷ có nhiều biến động thời tiết đáng chú ý (liên quan đến kỷ nguyên Dust Bowl tại Mỹ). Sự khác biệt hoặc tương đồng giữa 6 trạm đo lường giúp đánh giá xem hiện tượng hạn hán hay mưa lớn diễn ra cục bộ tại một số vùng hay diễn ra trên diện rộng toàn tiểu bang.
