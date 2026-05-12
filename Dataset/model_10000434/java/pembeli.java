





import java.util.List;
import java.util.ArrayList;

public class pembeli  {

    private String password;
    private String name;
    private String mail;
    private String shippinginfo;
    private String username;
    private String address;
    private String id;



    public pembeli(
        String password,        String name,        String mail,        String shippinginfo,        String username,        String address,        String id    ) {
        this.password = password;
        this.name = name;
        this.mail = mail;
        this.shippinginfo = shippinginfo;
        this.username = username;
        this.address = address;
        this.id = id;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}