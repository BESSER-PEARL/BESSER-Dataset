





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;
    private String password;
    private int u_id;
    private String e_mail;
    private String phone;



    public User(
        String name,        String password,        int u_id,        String e_mail,        String phone    ) {
        this.name = name;
        this.password = password;
        this.u_id = u_id;
        this.e_mail = e_mail;
        this.phone = phone;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getU_id() {
        return u_id;
    }

    public void setU_id(int u_id) {
        this.u_id = u_id;
    }
    public String getE_mail() {
        return e_mail;
    }

    public void setE_mail(String e_mail) {
        this.e_mail = e_mail;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }


}