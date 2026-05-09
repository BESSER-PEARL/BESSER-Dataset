





import java.util.List;
import java.util.ArrayList;

public class CodePack_Shared_ContactData  {

    private int phone_no;
    private String e_mail;
    private String full_name;



    public CodePack_Shared_ContactData(
        int phone_no,        String e_mail,        String full_name    ) {
        this.phone_no = phone_no;
        this.e_mail = e_mail;
        this.full_name = full_name;
    }


    public int getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(int phone_no) {
        this.phone_no = phone_no;
    }
    public String getE_mail() {
        return e_mail;
    }

    public void setE_mail(String e_mail) {
        this.e_mail = e_mail;
    }
    public String getFull_name() {
        return full_name;
    }

    public void setFull_name(String full_name) {
        this.full_name = full_name;
    }


}