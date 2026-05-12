





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Password;
    private String Fname;
    private String email;
    private String Lname;





    private ILogin_Interface ilogin_interface;




    private Binary_File binary_file;


    public User(
        String Password,        String Fname,        String email,        String Lname    ) {
        this.Password = Password;
        this.Fname = Fname;
        this.email = email;
        this.Lname = Lname;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getFname() {
        return Fname;
    }

    public void setFname(String Fname) {
        this.Fname = Fname;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLname() {
        return Lname;
    }

    public void setLname(String Lname) {
        this.Lname = Lname;
    }

    public ILogin_Interface getIlogin_interface() {
        return ilogin_interface;
    }

    public void setIlogin_interface(ILogin_Interface ilogin_interface) {
        this.ilogin_interface = ilogin_interface;
    }
    public Binary_File getBinary_file() {
        return binary_file;
    }

    public void setBinary_file(Binary_File binary_file) {
        this.binary_file = binary_file;
    }

}