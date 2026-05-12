





import java.util.List;
import java.util.ArrayList;

public class Admin  {






    private Student student;




    private Account account;




    private Message message;




    private HomePage homepage;


    public Admin(
    ) {
    }



    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public Message getMessage() {
        return message;
    }

    public void setMessage(Message message) {
        this.message = message;
    }
    public HomePage getHomepage() {
        return homepage;
    }

    public void setHomepage(HomePage homepage) {
        this.homepage = homepage;
    }

}