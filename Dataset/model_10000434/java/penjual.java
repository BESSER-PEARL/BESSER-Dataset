





import java.util.List;
import java.util.ArrayList;

public class penjual  {

    private String id;
    private String username;
    private String bussinessname;
    private String address;
    private String mail;
    private String bank;
    private String password;
    private String name;
    private String shippinginfo;





    private User user;


    public penjual(
        String id,        String username,        String bussinessname,        String address,        String mail,        String bank,        String password,        String name,        String shippinginfo    ) {
        this.id = id;
        this.username = username;
        this.bussinessname = bussinessname;
        this.address = address;
        this.mail = mail;
        this.bank = bank;
        this.password = password;
        this.name = name;
        this.shippinginfo = shippinginfo;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getBussinessname() {
        return bussinessname;
    }

    public void setBussinessname(String bussinessname) {
        this.bussinessname = bussinessname;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}