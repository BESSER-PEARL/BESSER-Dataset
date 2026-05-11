





import java.util.List;
import java.util.ArrayList;

public class training_Trainer extends Person {






    private List<training_Training> training_trainings;




    private training_Training training_training;




    private training_Session training_session;


    public training_Trainer(
    ) {
        super(
        );
        this.training_trainings = new ArrayList<>();
    }

    public training_Trainer(
        ArrayList<training_Training> training_trainings    ) {
        this.training_trainings = training_trainings;
    }


    public List<training_Training> getTraining_trainings() {
        return training_trainings;
    }

    public void addTraining_training(Training_training training_training) {
        this.training_trainings.add(training_training);
    }
    public training_Training getTraining_training() {
        return training_training;
    }

    public void setTraining_training(training_Training training_training) {
        this.training_training = training_training;
    }
    public training_Session getTraining_session() {
        return training_session;
    }

    public void setTraining_session(training_Session training_session) {
        this.training_session = training_session;
    }

}