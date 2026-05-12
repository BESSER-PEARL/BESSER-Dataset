





import java.util.List;
import java.util.ArrayList;

public class SinhVien  {

    private String nganhhoc;
    private String lop;
    private String MSSV;
    private String bomon;





    private Customer customer;


    public SinhVien(
        String nganhhoc,        String lop,        String MSSV,        String bomon    ) {
        this.nganhhoc = nganhhoc;
        this.lop = lop;
        this.MSSV = MSSV;
        this.bomon = bomon;
    }


    public String getNganhhoc() {
        return nganhhoc;
    }

    public void setNganhhoc(String nganhhoc) {
        this.nganhhoc = nganhhoc;
    }
    public String getLop() {
        return lop;
    }

    public void setLop(String lop) {
        this.lop = lop;
    }
    public String getMssv() {
        return MSSV;
    }

    public void setMssv(String MSSV) {
        this.MSSV = MSSV;
    }
    public String getBomon() {
        return bomon;
    }

    public void setBomon(String bomon) {
        this.bomon = bomon;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}