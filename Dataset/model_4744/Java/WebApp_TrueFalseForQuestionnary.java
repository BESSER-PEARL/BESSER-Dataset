





import java.util.List;
import java.util.ArrayList;

public class WebApp_TrueFalseForQuestionnary extends TrueFalse {

    private String correct;



    public WebApp_TrueFalseForQuestionnary(
        String correct    ) {
        super(
        );
        this.correct = correct;
    }


    public String getCorrect() {
        return correct;
    }

    public void setCorrect(String correct) {
        this.correct = correct;
    }


}