





import java.util.List;
import java.util.ArrayList;

public class textualusecase_Step  {

    private String name;





    private List<textualusecase_AlternativeFlow> textualusecase_alternativeflows;




    private textualusecase_AlternativeFlow textualusecase_alternativeflow;


    public textualusecase_Step(
        String name    ) {
        this.name = name;
        this.textualusecase_alternativeflows = new ArrayList<>();
    }

    public textualusecase_Step(
        String name        ArrayList<textualusecase_AlternativeFlow> textualusecase_alternativeflows    ) {
        this.name = name;
        this.textualusecase_alternativeflows = textualusecase_alternativeflows;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<textualusecase_AlternativeFlow> getTextualusecase_alternativeflows() {
        return textualusecase_alternativeflows;
    }

    public void addTextualusecase_alternativeflow(Textualusecase_alternativeflow textualusecase_alternativeflow) {
        this.textualusecase_alternativeflows.add(textualusecase_alternativeflow);
    }
    public textualusecase_AlternativeFlow getTextualusecase_alternativeflow() {
        return textualusecase_alternativeflow;
    }

    public void setTextualusecase_alternativeflow(textualusecase_AlternativeFlow textualusecase_alternativeflow) {
        this.textualusecase_alternativeflow = textualusecase_alternativeflow;
    }

}