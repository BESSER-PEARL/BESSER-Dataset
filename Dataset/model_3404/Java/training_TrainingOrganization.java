





import java.util.List;
import java.util.ArrayList;

public class training_TrainingOrganization  {

    private String name;





    private List<training_Person> training_persons;




    private List<training_Session> training_sessions;


    public training_TrainingOrganization(
        String name    ) {
        this.name = name;
        this.training_persons = new ArrayList<>();
        this.training_sessions = new ArrayList<>();
    }

    public training_TrainingOrganization(
        String name        ArrayList<training_Person> training_persons,        ArrayList<training_Session> training_sessions    ) {
        this.name = name;
        this.training_persons = training_persons;
        this.training_sessions = training_sessions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<training_Person> getTraining_persons() {
        return training_persons;
    }

    public void addTraining_person(Training_person training_person) {
        this.training_persons.add(training_person);
    }
    public List<training_Session> getTraining_sessions() {
        return training_sessions;
    }

    public void addTraining_session(Training_session training_session) {
        this.training_sessions.add(training_session);
    }

}