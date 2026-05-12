





import java.util.List;
import java.util.ArrayList;

public class penjual  {

    private String bank;
    private String password;
    private String address;
    private String shippinginfo;
    private String bussinessname;
    private String id;
    private String mail;
    private String name;
    private String username;





    private User user;


    public penjual(
        String bank,        String password,        String address,        String shippinginfo,        String bussinessname,        String id,        String mail,        String name,        String username    ) {
        this.bank = bank;
        this.password = password;
        this.address = address;
        this.shippinginfo = shippinginfo;
        this.bussinessname = bussinessname;
        this.id = id;
        this.mail = mail;
        this.name = name;
        this.username = username;
    }


    public String getBank() {
        return bank;
    }

    public void setBank(String bank) {
        this.bank = bank;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public String getBussinessname() {
        return bussinessname;
    }

    public void setBussinessname(String bussinessname) {
        this.bussinessname = bussinessname;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}