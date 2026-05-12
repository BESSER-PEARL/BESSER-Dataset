





import java.util.List;
import java.util.ArrayList;

public class mypackage_Perosn  {

    private int age;
    private String lname;
    private int id;
    private String Pass;
    private String UserName;
    private String fName;



    public mypackage_Perosn(
        int age,        String lname,        int id,        String Pass,        String UserName,        String fName    ) {
        this.age = age;
        this.lname = lname;
        this.id = id;
        this.Pass = Pass;
        this.UserName = UserName;
        this.fName = fName;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPass() {
        return Pass;
    }

    public void setPass(String Pass) {
        this.Pass = Pass;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getFname() {
        return fName;
    }

    public void setFname(String fName) {
        this.fName = fName;
    }


}