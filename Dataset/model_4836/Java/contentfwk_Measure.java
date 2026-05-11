





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Measure extends Element {






    private contentfwk_Measure contentfwk_measure;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Objective> contentfwk_objectives;




    private contentfwk_Objective contentfwk_objective;


    public contentfwk_Measure(
    ) {
        super(
        );
        this.contentfwk_objectives = new ArrayList<>();
    }

    public contentfwk_Measure(
        ArrayList<contentfwk_Objective> contentfwk_objectives    ) {
        this.contentfwk_objectives = contentfwk_objectives;
    }


    public contentfwk_Measure getContentfwk_measure() {
        return contentfwk_measure;
    }

    public void setContentfwk_measure(contentfwk_Measure contentfwk_measure) {
        this.contentfwk_measure = contentfwk_measure;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Objective> getContentfwk_objectives() {
        return contentfwk_objectives;
    }

    public void addContentfwk_objective(Contentfwk_objective contentfwk_objective) {
        this.contentfwk_objectives.add(contentfwk_objective);
    }
    public contentfwk_Objective getContentfwk_objective() {
        return contentfwk_objective;
    }

    public void setContentfwk_objective(contentfwk_Objective contentfwk_objective) {
        this.contentfwk_objective = contentfwk_objective;
    }

}