





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_StaffMember  {

    private String password;
    private String pers_no;
    private String full_name;
    private int phone_no;
    private String email;
    private String role_name;



    public CodePack_DataModels_StaffMember(
        String password,        String pers_no,        String full_name,        int phone_no,        String email,        String role_name    ) {
        this.password = password;
        this.pers_no = pers_no;
        this.full_name = full_name;
        this.phone_no = phone_no;
        this.email = email;
        this.role_name = role_name;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getPers_no() {
        return pers_no;
    }

    public void setPers_no(String pers_no) {
        this.pers_no = pers_no;
    }
    public String getFull_name() {
        return full_name;
    }

    public void setFull_name(String full_name) {
        this.full_name = full_name;
    }
    public int getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(int phone_no) {
        this.phone_no = phone_no;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getRole_name() {
        return role_name;
    }

    public void setRole_name(String role_name) {
        this.role_name = role_name;
    }


}