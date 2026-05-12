





import java.util.List;
import java.util.ArrayList;

public class mypackage_Perosn  {

    private String fName;
    private int id;
    private String lname;
    private String UserName;
    private int age;



    public mypackage_Perosn(
        String fName,        int id,        String lname,        String UserName,        int age    ) {
        this.fName = fName;
        this.id = id;
        this.lname = lname;
        this.UserName = UserName;
        this.age = age;
    }


    public String getFname() {
        return fName;
    }

    public void setFname(String fName) {
        this.fName = fName;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}