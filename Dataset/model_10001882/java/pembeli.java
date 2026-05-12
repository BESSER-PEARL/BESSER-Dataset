





import java.util.List;
import java.util.ArrayList;

public class pembeli  {

    private String id;
    private String name;
    private String username;
    private String password;
    private String shippinginfo;
    private String mail;
    private String address;



    public pembeli(
        String id,        String name,        String username,        String password,        String shippinginfo,        String mail,        String address    ) {
        this.id = id;
        this.name = name;
        this.username = username;
        this.password = password;
        this.shippinginfo = shippinginfo;
        this.mail = mail;
        this.address = address;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}