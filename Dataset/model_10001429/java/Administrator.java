





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String username;
    private String phone;
    private String e_mail;
    private int u_id;



    public Administrator(
        String username,        String phone,        String e_mail,        int u_id    ) {
        this.username = username;
        this.phone = phone;
        this.e_mail = e_mail;
        this.u_id = u_id;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getE_mail() {
        return e_mail;
    }

    public void setE_mail(String e_mail) {
        this.e_mail = e_mail;
    }
    public int getU_id() {
        return u_id;
    }

    public void setU_id(int u_id) {
        this.u_id = u_id;
    }


}