





import java.util.List;
import java.util.ArrayList;

public class training_Training  {

    private String title;





    private List<training_Trainer> training_trainers;




    private training_Session training_session;




    private training_Trainer training_trainer;




    private training_TrainingOrganization training_trainingorganization;


    public training_Training(
        String title    ) {
        this.title = title;
        this.training_trainers = new ArrayList<>();
    }

    public training_Training(
        String title        ArrayList<training_Trainer> training_trainers    ) {
        this.title = title;
        this.training_trainers = training_trainers;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<training_Trainer> getTraining_trainers() {
        return training_trainers;
    }

    public void addTraining_trainer(Training_trainer training_trainer) {
        this.training_trainers.add(training_trainer);
    }
    public training_Session getTraining_session() {
        return training_session;
    }

    public void setTraining_session(training_Session training_session) {
        this.training_session = training_session;
    }
    public training_Trainer getTraining_trainer() {
        return training_trainer;
    }

    public void setTraining_trainer(training_Trainer training_trainer) {
        this.training_trainer = training_trainer;
    }
    public training_TrainingOrganization getTraining_trainingorganization() {
        return training_trainingorganization;
    }

    public void setTraining_trainingorganization(training_TrainingOrganization training_trainingorganization) {
        this.training_trainingorganization = training_trainingorganization;
    }

}