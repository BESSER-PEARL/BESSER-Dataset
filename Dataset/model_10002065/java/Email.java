





import java.util.List;
import java.util.ArrayList;

public class Email  {






    private Student student;




    private ILogin_Interface ilogin_interface;




    private Admin admin;


    public Email(
    ) {
    }



    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public ILogin_Interface getIlogin_interface() {
        return ilogin_interface;
    }

    public void setIlogin_interface(ILogin_Interface ilogin_interface) {
        this.ilogin_interface = ilogin_interface;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}