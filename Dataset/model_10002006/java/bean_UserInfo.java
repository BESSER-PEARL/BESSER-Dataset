





import java.util.List;
import java.util.ArrayList;

public class bean_UserInfo  {

    private String dob;
    private String gender;
    private String password;
    private String email;
    private String last;
    private String first;
    private String local;
    private String phone;
    private String permanent;



    public bean_UserInfo(
        String dob,        String gender,        String password,        String email,        String last,        String first,        String local,        String phone,        String permanent    ) {
        this.dob = dob;
        this.gender = gender;
        this.password = password;
        this.email = email;
        this.last = last;
        this.first = first;
        this.local = local;
        this.phone = phone;
        this.permanent = permanent;
    }


    public String getDob() {
        return dob;
    }

    public void setDob(String dob) {
        this.dob = dob;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLast() {
        return last;
    }

    public void setLast(String last) {
        this.last = last;
    }
    public String getFirst() {
        return first;
    }

    public void setFirst(String first) {
        this.first = first;
    }
    public String getLocal() {
        return local;
    }

    public void setLocal(String local) {
        this.local = local;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getPermanent() {
        return permanent;
    }

    public void setPermanent(String permanent) {
        this.permanent = permanent;
    }


}