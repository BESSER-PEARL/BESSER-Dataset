





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String password_;
    private String username_;





    private Person person;


    public Login(
        String password_,        String username_    ) {
        this.password_ = password_;
        this.username_ = username_;
    }


    public String getPassword_() {
        return password_;
    }

    public void setPassword_(String password_) {
        this.password_ = password_;
    }
    public String getUsername_() {
        return username_;
    }

    public void setUsername_(String username_) {
        this.username_ = username_;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}