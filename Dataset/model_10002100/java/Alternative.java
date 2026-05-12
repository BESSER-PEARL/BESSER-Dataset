





import java.util.List;
import java.util.ArrayList;

public class Alternative  {

    private None step;
    private String answer;
    private String content;
    private None category;
    private String answer_text;





    private AlternativeCategory alternativecategory;




    private Step step;


    public Alternative(
        None step,        String answer,        String content,        None category,        String answer_text    ) {
        this.step = step;
        this.answer = answer;
        this.content = content;
        this.category = category;
        this.answer_text = answer_text;
    }


    public None getStep() {
        return step;
    }

    public void setStep(None step) {
        this.step = step;
    }
    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public None getCategory() {
        return category;
    }

    public void setCategory(None category) {
        this.category = category;
    }
    public String getAnswer_text() {
        return answer_text;
    }

    public void setAnswer_text(String answer_text) {
        this.answer_text = answer_text;
    }

    public AlternativeCategory getAlternativecategory() {
        return alternativecategory;
    }

    public void setAlternativecategory(AlternativeCategory alternativecategory) {
        this.alternativecategory = alternativecategory;
    }
    public Step getStep() {
        return step;
    }

    public void setStep(Step step) {
        this.step = step;
    }

}