





import java.util.List;
import java.util.ArrayList;

public class training_TrainingOrganization  {

    private String name;





    private List<training_Training> training_trainings;




    private List<training_Session> training_sessions;


    public training_TrainingOrganization(
        String name    ) {
        this.name = name;
        this.training_trainings = new ArrayList<>();
        this.training_sessions = new ArrayList<>();
    }

    public training_TrainingOrganization(
        String name        ArrayList<training_Training> training_trainings,        ArrayList<training_Session> training_sessions    ) {
        this.name = name;
        this.training_trainings = training_trainings;
        this.training_sessions = training_sessions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<training_Training> getTraining_trainings() {
        return training_trainings;
    }

    public void addTraining_training(Training_training training_training) {
        this.training_trainings.add(training_training);
    }
    public List<training_Session> getTraining_sessions() {
        return training_sessions;
    }

    public void addTraining_session(Training_session training_session) {
        this.training_sessions.add(training_session);
    }

}