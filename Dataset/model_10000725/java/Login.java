





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private None login;
    private String Username;
    private String Password;





    private Student student;




    private Faculty faculty;


    public Login(
        None login,        String Username,        String Password    ) {
        this.login = login;
        this.Username = Username;
        this.Password = Password;
    }


    public None getLogin() {
        return login;
    }

    public void setLogin(None login) {
        this.login = login;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public Faculty getFaculty() {
        return faculty;
    }

    public void setFaculty(Faculty faculty) {
        this.faculty = faculty;
    }

}