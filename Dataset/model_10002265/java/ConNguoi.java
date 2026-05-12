




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ConNguoi  {

    private String CMND;
    private String hoten;
    private String diachi;
    private LocalDate ngaysinh;
    private boolean gioitinh;



    public ConNguoi(
        String CMND,        String hoten,        String diachi,        LocalDate ngaysinh,        boolean gioitinh    ) {
        this.CMND = CMND;
        this.hoten = hoten;
        this.diachi = diachi;
        this.ngaysinh = ngaysinh;
        this.gioitinh = gioitinh;
    }


    public String getCmnd() {
        return CMND;
    }

    public void setCmnd(String CMND) {
        this.CMND = CMND;
    }
    public String getHoten() {
        return hoten;
    }

    public void setHoten(String hoten) {
        this.hoten = hoten;
    }
    public String getDiachi() {
        return diachi;
    }

    public void setDiachi(String diachi) {
        this.diachi = diachi;
    }
    public LocalDate getNgaysinh() {
        return ngaysinh;
    }

    public void setNgaysinh(LocalDate ngaysinh) {
        this.ngaysinh = ngaysinh;
    }
    public boolean getGioitinh() {
        return gioitinh;
    }

    public void setGioitinh(boolean gioitinh) {
        this.gioitinh = gioitinh;
    }


}