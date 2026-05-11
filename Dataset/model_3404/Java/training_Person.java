





import java.util.List;
import java.util.ArrayList;

public class training_Person  {

    private String lastname;
    private String firstname;





    private training_Session training_session;


    public training_Person(
        String lastname,        String firstname    ) {
        this.lastname = lastname;
        this.firstname = firstname;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public training_Session getTraining_session() {
        return training_session;
    }

    public void setTraining_session(training_Session training_session) {
        this.training_session = training_session;
    }

}