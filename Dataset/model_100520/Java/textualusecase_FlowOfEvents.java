





import java.util.List;
import java.util.ArrayList;

public class textualusecase_FlowOfEvents  {

    private String name;





    private textualusecase_Step textualusecase_step;




    private List<textualusecase_Step> textualusecase_steps;


    public textualusecase_FlowOfEvents(
        String name    ) {
        this.name = name;
        this.textualusecase_steps = new ArrayList<>();
    }

    public textualusecase_FlowOfEvents(
        String name        ArrayList<textualusecase_Step> textualusecase_steps    ) {
        this.name = name;
        this.textualusecase_steps = textualusecase_steps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public textualusecase_Step getTextualusecase_step() {
        return textualusecase_step;
    }

    public void setTextualusecase_step(textualusecase_Step textualusecase_step) {
        this.textualusecase_step = textualusecase_step;
    }
    public List<textualusecase_Step> getTextualusecase_steps() {
        return textualusecase_steps;
    }

    public void addTextualusecase_step(Textualusecase_step textualusecase_step) {
        this.textualusecase_steps.add(textualusecase_step);
    }

}