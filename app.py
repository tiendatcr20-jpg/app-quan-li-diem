import streamlit as st
import pandas as pd

# 1. Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Tạo dữ liệu 10 sinh viên
data = {
    "Họ tên": ["An", "Bình", "Chi", "Dũng", "Hà", "Lan", "Minh", "Nam", "Phúc", "Trang"],
    "Chuyên cần": [9.0, 8.5, 7.0, 6.0, 9.5, 5.0, 8.0, 4.0, 9.0, 7.5],
    "Giữa kỳ": [8.0, 7.5, 6.5, 5.0, 9.0, 4.5, 7.0, 3.5, 8.5, 6.0],
    "Cuối kỳ": [8.5, 8.0, 7.0, 5.5, 9.5, 4.0, 7.5, 4.0, 8.0, 6.5]
}

df = pd.DataFrame(data)
df["Tong_ket"] = (df["Chuyên cần"] * 0.2 + df["Giữa kỳ"] * 0.3 + df["Cuối kỳ"] * 0.5).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 2. Hiển thị bảng điểm
st.subheader("📋 Bảng điểm sinh viên")
st.dataframe(df)
st.divider()

# 3. Hiển thị điểm trung bình của lớp
dtb_lop = df["Tong_ket"].mean()
st.metric("Điểm trung bình của lớp", f"{dtb_lop:.2f}")

# 4. Hiển thị sinh viên cao nhất và thấp nhất
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]

col1, col2 = st.columns(2)
with col1:
    st.success(f"🏆 **Điểm cao nhất:** {sv_cao_nhat['Họ tên']} ({sv_cao_nhat['Tong_ket']} điểm)")
with col2:
    st.error(f"⚠️ **Điểm thấp nhất:** {sv_thap_nhat['Họ tên']} ({sv_thap_nhat['Tong_ket']} điểm)")

# 5. Hiển thị số sinh viên đạt (>= 5.0)
so_sv_dat = (df["Tong_ket"] >= 5.0).sum()
st.info(f"📊 **Số sinh viên đạt (>= 5.0):** {so_sv_dat}/{len(df)} sinh viên")
st.divider()

# 3. Hiển thị điểm trung bình của lớp
dtb_lop = df["Tong_ket"].mean()
st.metric("Điểm trung bình của lớp", f"{dtb_lop:.2f}")

# 4. Hiển thị sinh viên cao nhất và thấp nhất
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]

col1, col2 = st.columns(2)
with col1:
    st.success(f"🏆 **Điểm cao nhất:** {sv_cao_nhat['Họ tên']} ({sv_cao_nhat['Tong_ket']} điểm)")
with col2:
    st.error(f"⚠️ **Điểm thấp nhất:** {sv_thap_nhat['Họ tên']} ({sv_thap_nhat['Tong_ket']} điểm)")

# 5. Hiển thị số sinh viên đạt (>= 5.0)
so_sv_dat = (df["Tong_ket"] >= 5.0).sum()
st.info(f"📊 **Số sinh viên đạt (>= 5.0):** {so_sv_dat}/{len(df)} sinh viên")
st.divider()

# 6 & 7. Tạo Selectbox chọn sinh viên và hiển thị chi tiết
st.subheader("🔍 Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn sinh viên:", df["Họ tên"])

if selected_student:
    sv_info = df[df["Họ tên"] == selected_student].iloc[0]
    st.write(f"**Chuyên cần:** {sv_info['Chuyên cần']}")
    st.write(f"**Giữa kỳ:** {sv_info['Giữa kỳ']}")
    st.write(f"**Cuối kỳ:** {sv_info['Cuối kỳ']}")
    st.write(f"**Điểm tổng kết:** {sv_info['Tong_ket']}")
    st.write(f"**Xếp loại:** {sv_info['Xep_loai']}")
st.divider()

# 8. Hiển thị biểu đồ cột điểm tổng kết
st.subheader("📈 Biểu đồ điểm tổng kết")
st.bar_chart(df.set_index("Họ tên")["Tong_ket"])
st.divider()

# 9. Họ tên và MSSV ở cuối trang
st.caption("Ứng dụng được tạo bởi: **[Điền Họ và Tên bạn]** - MSSV: **[Điền MSSV]**")

# 9. Họ tên và MSSV ở cuối trang
st.caption("Ứng dụng được tạo bởi: **[Điền Họ và Tên bạn]** - MSSV: **[Điền MSSV]**")

# 9. Họ tên và MSSV ở cuối trang
st.caption("Ứng dụng được tạo bởi: **[Điền Họ và Tên bạn]** - MSSV: **[Điền MSSV]**")
