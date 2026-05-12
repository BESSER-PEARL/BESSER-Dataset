





import java.util.List;
import java.util.ArrayList;

public class coustomer  {

    private String shippinginfo;
    private String address;
    private int customerId;
    private String name;
    private int phoneno;
    private String email;



    public coustomer(
        String shippinginfo,        String address,        int customerId,        String name,        int phoneno,        String email    ) {
        this.shippinginfo = shippinginfo;
        this.address = address;
        this.customerId = customerId;
        this.name = name;
        this.phoneno = phoneno;
        this.email = email;
    }


    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}