





import java.util.List;
import java.util.ArrayList;

public class textualusecase_Statement extends Step {






    private textualusecase_Step textualusecase_step;




    private textualusecase_Condition textualusecase_condition;




    private List<textualusecase_Step> textualusecase_steps;


    public textualusecase_Statement(
    ) {
        super(
        );
        this.textualusecase_steps = new ArrayList<>();
    }

    public textualusecase_Statement(
        ArrayList<textualusecase_Step> textualusecase_steps    ) {
        this.textualusecase_steps = textualusecase_steps;
    }


    public textualusecase_Step getTextualusecase_step() {
        return textualusecase_step;
    }

    public void setTextualusecase_step(textualusecase_Step textualusecase_step) {
        this.textualusecase_step = textualusecase_step;
    }
    public textualusecase_Condition getTextualusecase_condition() {
        return textualusecase_condition;
    }

    public void setTextualusecase_condition(textualusecase_Condition textualusecase_condition) {
        this.textualusecase_condition = textualusecase_condition;
    }
    public List<textualusecase_Step> getTextualusecase_steps() {
        return textualusecase_steps;
    }

    public void addTextualusecase_step(Textualusecase_step textualusecase_step) {
        this.textualusecase_steps.add(textualusecase_step);
    }

}