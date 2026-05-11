





import java.util.List;
import java.util.ArrayList;

public class WebApp_GroupOfQuestions extends Question {

    private String name;





    private List<WebApp_Question> webapp_questions;


    public WebApp_GroupOfQuestions(
        String name    ) {
        super(
        );
        this.name = name;
        this.webapp_questions = new ArrayList<>();
    }

    public WebApp_GroupOfQuestions(
        String name        ArrayList<WebApp_Question> webapp_questions    ) {
        this.name = name;
        this.webapp_questions = webapp_questions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<WebApp_Question> getWebapp_questions() {
        return webapp_questions;
    }

    public void addWebapp_question(Webapp_question webapp_question) {
        this.webapp_questions.add(webapp_question);
    }

}