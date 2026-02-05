import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO

st.set_page_config(page_title="画像ツール", layout="wide")

col1, col2 = st.columns([0.08, 0.92])
with col1:
    try:
        logo = Image.open("logo.jpg")
        logo_resized = logo.resize((40, 40), Image.Resampling.LANCZOS)
        st.image(logo_resized, width=40)
    except:
        pass
with col2:
    st.title("📸 画像ツール")

tab1, tab2 = st.tabs(["画像ぼかし", "4分割+合成"])

# ===== タブ1：画像ぼかし =====
with tab1:
    st.subheader("画像をぼかす")
    
    st.write("アップロードされた画像を、指定した強度でぼかします。")
    
    uploaded_file = st.file_uploader("画像をアップロード", type=['png', 'jpg', 'jpeg', 'bmp', 'gif'], key="blur_upload")
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        original_width, original_height = img.size
        
        st.write(f"**元のサイズ:** {original_width} × {original_height}")
        
        # スライダーで強度を指定（0～100）
        strength = st.slider("ぼかしの強度", min_value=0, max_value=100, value=10, step=1, key="blur_strength")
        
        if strength > 0:
            # 強度をフィルタの半径に変換（0～50に正規化）
            blur_radius = int((strength / 100) * 50)
            
            # ぼかしを適用
            blurred_img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
            
            st.subheader("プレビュー")
            st.image(blurred_img, width=400)
            
            st.subheader("ダウンロード")
            
            buf = BytesIO()
            blurred_img.save(buf, format='PNG')
            buf.seek(0)
            
            st.download_button(
                label="📥 ぼかし済み画像をダウンロード",
                data=buf.getvalue(),
                file_name="blurred_image.png",
                mime="image/png",
                key="blur_download"
            )
        else:
            st.subheader("プレビュー")
            st.image(img, width=400)
            st.info("強度を0より大きい値に設定してください")
    else:
        st.info("👆 画像をアップロードしてください")

# ===== タブ2：4分割+合成 =====
with tab2:
    st.info("このタブは統合予定です")
