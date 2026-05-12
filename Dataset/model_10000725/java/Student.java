





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String First_Name;
    private String Username;
    private String ID;
    private String Password;
    private String Last_Name;



    public Student(
        String First_Name,        String Username,        String ID,        String Password,        String Last_Name    ) {
        this.First_Name = First_Name;
        this.Username = Username;
        this.ID = ID;
        this.Password = Password;
        this.Last_Name = Last_Name;
    }


    public String getFirst_name() {
        return First_Name;
    }

    public void setFirst_name(String First_Name) {
        this.First_Name = First_Name;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
    }


}