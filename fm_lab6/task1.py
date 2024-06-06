import img_utils as iu


src = 'fm_lab6/src'
img_path = f'{src}/4.png'

render_to = 'fm_lab6/renders/task1'
rimg_path = f'{render_to}/fft2.png'
reimg_path = f'{render_to}/new4.png'

corr_im_path = f'{src}/corr_fft2.png'
corrected = True

img = iu.read_img(img_path)
ans, ang, nzmm = iu.fft2_2img(img)
iu.save_img(ans, rimg_path)

if corrected:
    img2 = iu.read_img(corr_im_path)
    ans2 = iu.ifft2_2img(img2, ang, nzmm)
    iu.save_img(ans2, reimg_path)