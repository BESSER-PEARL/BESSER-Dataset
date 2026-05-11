





import java.util.List;
import java.util.ArrayList;

public class training_Person  {

    private String firstname;
    private String lastname;





    private training_TrainingOrganization training_trainingorganization;




    private training_Session training_session;


    public training_Person(
        String firstname,        String lastname    ) {
        this.firstname = firstname;
        this.lastname = lastname;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public training_TrainingOrganization getTraining_trainingorganization() {
        return training_trainingorganization;
    }

    public void setTraining_trainingorganization(training_TrainingOrganization training_trainingorganization) {
        this.training_trainingorganization = training_trainingorganization;
    }
    public training_Session getTraining_session() {
        return training_session;
    }

    public void setTraining_session(training_Session training_session) {
        this.training_session = training_session;
    }

}