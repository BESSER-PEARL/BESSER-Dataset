





import java.util.List;
import java.util.ArrayList;

public class Paper_User  {

    private int Age;
    private String Gender;
    private int UserID;
    private String UserName;



    public Paper_User(
        int Age,        String Gender,        int UserID,        String UserName    ) {
        this.Age = Age;
        this.Gender = Gender;
        this.UserID = UserID;
        this.UserName = UserName;
    }


    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}