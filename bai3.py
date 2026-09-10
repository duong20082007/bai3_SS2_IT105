# Danh mục 7 giai đoạn SDLC & Sản phẩm đầu ra
# Giai đoạn     | cốt lõi                                                   |   đầu ra
# Planning      | Đánh giá tính khả thi,                                    |   Feasibility Study
#               | nguồn lực và rủi ro của việc                              |
#               | tự động hóa báo cáo thù lao                               |
# Analysis      | Thu thập quy tắc tính toán chi tiết:                      |   Tài liệu Đặc tả Yêu cầu Nghiệp vụ (BRD),
#               | giá 20.000đ/đơn, thưởng 10% nếu > 50 đơn, và đặc biệt     |   Tài liệu Đặc tả Phần mềm (SRS)
#               | là quy trình xử lý đơn có trạng thái DISPUTED từ Tổng đài |
# Design        | Thiết kế logic xử lý bẫy tranh chấp                       |   Tài liệu Thiết kế Hệ thống (SDD), Sơ đồ luồng dữ liệu (DFD), Sơ đồ CSDL (ERD).
# Implementation| Làm rõ các edge cases (bẫy dữ liệu) để Dev code chính xác |   Mã nguồn (Source Code) đã hoàn thiện (do Dev thực hiện).
# Testing       | Phối hợp với QA để test bẫy tranh chấp và thưởng mốc.     |   Kịch bản kiểm thử (Test Cases), Báo cáo Lỗi (Bug Report), Biên bản Nghiệm thu UAT.
#                   Hỗ trợ UAT
# Deployment    | Theo dõi hệ thống chạy thực tế trong những tuần đầu tiên  |   Tài liệu Hướng dẫn sử dụng (User Manual), Hệ thống Live
# Maintenance   | Cập nhật yêu cầu khi chính sách thù lao thay đổi          |   Danh sách Yêu cầu Cập nhật (Change Requests), Phiên bản vá lỗi
#                   trong tương lai.


def calculate_driver_payout(transactions):
    payout_report = {}
    
    for tx in transactions:
        driver_id = tx['driver_id']
        status = tx['status']
        
        if driver_id not in payout_report:
            payout_report[driver_id] = {
                'successful_orders': 0,
                'disputed_orders': 0
            }
            
        if status == 'DELIVERED':
            payout_report[driver_id]['successful_orders'] = payout_report[driver_id]['successful_orders'] + 1
        elif status == 'DISPUTED':
            payout_report[driver_id]['disputed_orders'] = payout_report[driver_id]['disputed_orders'] + 1
            
    for driver_id in payout_report:
        so_don_thanh_cong = payout_report[driver_id]['successful_orders']
        so_don_tranh_chap = payout_report[driver_id]['disputed_orders']
        
        luong_co_ban = so_don_thanh_cong * 20000
        
        tien_thuong = 0
        if so_don_thanh_cong > 50:
            tien_thuong = luong_co_ban * 0.10
            
        tong_thuc_nhan = luong_co_ban + tien_thuong
        
        tien_tam_giu = so_don_tranh_chap * 20000
        
        payout_report[driver_id]['base_pay'] = luong_co_ban
        payout_report[driver_id]['bonus_amount'] = tien_thuong
        payout_report[driver_id]['total_payout'] = tong_thuc_nhan
        payout_report[driver_id]['held_amount'] = tien_tam_giu
        
    return payout_report

sample_transactions = []

for i in range(51):
    sample_transactions.append({'driver_id': 'TX_A', 'status': 'DELIVERED'})
sample_transactions.append({'driver_id': 'TX_A', 'status': 'DISPUTED'})

for i in range(30):
    sample_transactions.append({'driver_id': 'TX_B', 'status': 'DELIVERED'})

sample_transactions.append({'driver_id': 'TX_C', 'status': 'DELIVERED'})
sample_transactions.append({'driver_id': 'TX_C', 'status': 'DELIVERED'})
sample_transactions.append({'driver_id': 'TX_C', 'status': 'DISPUTED'})
sample_transactions.append({'driver_id': 'TX_C', 'status': 'DISPUTED'})
sample_transactions.append({'driver_id': 'TX_C', 'status': 'DISPUTED'})

report = calculate_driver_payout(sample_transactions)

for driver_id in report:
    data = report[driver_id]
    print("--- Báo cáo tài xế", driver_id, "---")
    print("Đơn thành công :", data['successful_orders'], "(Cơ bản:", data['base_pay'], "đ)")
    print("Tiền thưởng    :", data['bonus_amount'], "đ")
    print("Tổng thực nhận :", data['total_payout'], "đ")
    print("Đơn tranh chấp :", data['disputed_orders'], "(Tạm giữ:", data['held_amount'], "đ)")
    print("")