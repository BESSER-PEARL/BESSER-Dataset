





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String first_Name;
    private String password;
    private String user_Name;
    private String last_Name;
    private int phone_Number;



    public Profile(
        String first_Name,        String password,        String user_Name,        String last_Name,        int phone_Number    ) {
        this.first_Name = first_Name;
        this.password = password;
        this.user_Name = user_Name;
        this.last_Name = last_Name;
        this.phone_Number = phone_Number;
    }


    public String getFirst_name() {
        return first_Name;
    }

    public void setFirst_name(String first_Name) {
        this.first_Name = first_Name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUser_name() {
        return user_Name;
    }

    public void setUser_name(String user_Name) {
        this.user_Name = user_Name;
    }
    public String getLast_name() {
        return last_Name;
    }

    public void setLast_name(String last_Name) {
        this.last_Name = last_Name;
    }
    public int getPhone_number() {
        return phone_Number;
    }

    public void setPhone_number(int phone_Number) {
        this.phone_Number = phone_Number;
    }


}