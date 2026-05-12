





import java.util.List;
import java.util.ArrayList;

public class Feedback  {

    private String feedback;
    private None alternative;
    private int level;
    private boolean state;





    private Alternative alternative;


    public Feedback(
        String feedback,        None alternative,        int level,        boolean state    ) {
        this.feedback = feedback;
        this.alternative = alternative;
        this.level = level;
        this.state = state;
    }


    public String getFeedback() {
        return feedback;
    }

    public void setFeedback(String feedback) {
        this.feedback = feedback;
    }
    public None getAlternative() {
        return alternative;
    }

    public void setAlternative(None alternative) {
        this.alternative = alternative;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public boolean getState() {
        return state;
    }

    public void setState(boolean state) {
        this.state = state;
    }

    public Alternative getAlternative() {
        return alternative;
    }

    public void setAlternative(Alternative alternative) {
        this.alternative = alternative;
    }

}