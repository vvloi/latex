#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt

out_dir = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'market_share_platforms.png')

# Dữ liệu ước tính từ SimilarWeb traffic ranking (2026) + báo cáo ngành công khai
# Shopee, Lazada, Tiki là 3 sàn lớn; Sendo, TikTok Shop, và các sàn khác (Chợ Tốt, Amazon, BachHoaXanh, v.v.)
platforms = ['Shopee', 'Lazada', 'Tiki', 'Sendo', 'TikTok Shop', 'Khác']
shares = [28, 20, 14, 10, 7, 21]

fig, ax = plt.subplots(figsize=(9,6))
colors = ['#EE4D2D', '#0B4DCA', '#0099CC', '#FF6600', '#000000', '#CCCCCC']
wedges, texts, autotexts = ax.pie(shares, labels=platforms, autopct='%1.1f%%', startangle=90, colors=colors)

# Định dạng text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

ax.set_title('Thị phần sàn TMĐT Việt Nam\nNguồn: SimilarWeb traffic ranking (2026) + báo cáo ngành công khai', fontsize=12, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig(out_path, dpi=150)
print('Saved', out_path)
