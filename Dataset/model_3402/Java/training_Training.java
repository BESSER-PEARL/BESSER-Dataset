





import java.util.List;
import java.util.ArrayList;

public class training_Training  {

    private String title;





    private training_Session training_session;


    public training_Training(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public training_Session getTraining_session() {
        return training_session;
    }

    public void setTraining_session(training_Session training_session) {
        this.training_session = training_session;
    }

}