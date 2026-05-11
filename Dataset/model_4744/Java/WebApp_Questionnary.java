





import java.util.List;
import java.util.ArrayList;

public class WebApp_Questionnary extends PageS_Q {

    private boolean feedback;



    public WebApp_Questionnary(
        boolean feedback    ) {
        super(
        );
        this.feedback = feedback;
    }


    public boolean getFeedback() {
        return feedback;
    }

    public void setFeedback(boolean feedback) {
        this.feedback = feedback;
    }


}