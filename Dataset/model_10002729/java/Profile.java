





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private int phone_Number;
    private String user_Name;
    private String last_Name;
    private String password;
    private String first_Name;



    public Profile(
        int phone_Number,        String user_Name,        String last_Name,        String password,        String first_Name    ) {
        this.phone_Number = phone_Number;
        this.user_Name = user_Name;
        this.last_Name = last_Name;
        this.password = password;
        this.first_Name = first_Name;
    }


    public int getPhone_number() {
        return phone_Number;
    }

    public void setPhone_number(int phone_Number) {
        this.phone_Number = phone_Number;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getFirst_name() {
        return first_Name;
    }

    public void setFirst_name(String first_Name) {
        this.first_Name = first_Name;
    }


}