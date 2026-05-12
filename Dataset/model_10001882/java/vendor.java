





import java.util.List;
import java.util.ArrayList;

public class vendor  {

    private String password;
    private String mail;
    private String name;
    private int id;
    private String bank;
    private String address;
    private String bussinessname;
    private int id_role;
    private String username;
    private String shippinginfo;





    private user user;


    public vendor(
        String password,        String mail,        String name,        int id,        String bank,        String address,        String bussinessname,        int id_role,        String username,        String shippinginfo    ) {
        this.password = password;
        this.mail = mail;
        this.name = name;
        this.id = id;
        this.bank = bank;
        this.address = address;
        this.bussinessname = bussinessname;
        this.id_role = id_role;
        this.username = username;
        this.shippinginfo = shippinginfo;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getBank() {
        return bank;
    }

    public void setBank(String bank) {
        this.bank = bank;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getBussinessname() {
        return bussinessname;
    }

    public void setBussinessname(String bussinessname) {
        this.bussinessname = bussinessname;
    }
    public int getId_role() {
        return id_role;
    }

    public void setId_role(int id_role) {
        this.id_role = id_role;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}