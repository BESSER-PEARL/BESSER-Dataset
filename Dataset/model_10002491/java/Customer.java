





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String c_address;
    private int c_id;
    private int c_mobile;
    private String c_email;
    private String c_name;



    public Customer(
        String c_address,        int c_id,        int c_mobile,        String c_email,        String c_name    ) {
        this.c_address = c_address;
        this.c_id = c_id;
        this.c_mobile = c_mobile;
        this.c_email = c_email;
        this.c_name = c_name;
    }


    public String getC_address() {
        return c_address;
    }

    public void setC_address(String c_address) {
        this.c_address = c_address;
    }
    public int getC_id() {
        return c_id;
    }

    public void setC_id(int c_id) {
        this.c_id = c_id;
    }
    public int getC_mobile() {
        return c_mobile;
    }

    public void setC_mobile(int c_mobile) {
        this.c_mobile = c_mobile;
    }
    public String getC_email() {
        return c_email;
    }

    public void setC_email(String c_email) {
        this.c_email = c_email;
    }
    public String getC_name() {
        return c_name;
    }

    public void setC_name(String c_name) {
        this.c_name = c_name;
    }


}