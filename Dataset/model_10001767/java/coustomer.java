





import java.util.List;
import java.util.ArrayList;

public class coustomer  {

    private String email;
    private int phoneno;
    private String address;
    private String name;
    private String shippinginfo;
    private int customerId;



    public coustomer(
        String email,        int phoneno,        String address,        String name,        String shippinginfo,        int customerId    ) {
        this.email = email;
        this.phoneno = phoneno;
        this.address = address;
        this.name = name;
        this.shippinginfo = shippinginfo;
        this.customerId = customerId;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }


}