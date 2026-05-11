





import java.util.List;
import java.util.ArrayList;

public class WebApp_SimpleQuestion extends Question {

    private String QuestionText;
    private String visualRep;



    public WebApp_SimpleQuestion(
        String QuestionText,        String visualRep    ) {
        super(
        );
        this.QuestionText = QuestionText;
        this.visualRep = visualRep;
    }


    public String getQuestiontext() {
        return QuestionText;
    }

    public void setQuestiontext(String QuestionText) {
        this.QuestionText = QuestionText;
    }
    public String getVisualrep() {
        return visualRep;
    }

    public void setVisualrep(String visualRep) {
        this.visualRep = visualRep;
    }


}