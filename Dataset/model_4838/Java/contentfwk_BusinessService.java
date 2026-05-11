





import java.util.List;
import java.util.ArrayList;

public class contentfwk_BusinessService extends Element, Service {






    private List<contentfwk_Objective> contentfwk_objectives;


    public contentfwk_BusinessService(
    ) {
        super(
        );
        this.contentfwk_objectives = new ArrayList<>();
    }

    public contentfwk_BusinessService(
        ArrayList<contentfwk_Objective> contentfwk_objectives    ) {
        this.contentfwk_objectives = contentfwk_objectives;
    }


    public List<contentfwk_Objective> getContentfwk_objectives() {
        return contentfwk_objectives;
    }

    public void addContentfwk_objective(Contentfwk_objective contentfwk_objective) {
        this.contentfwk_objectives.add(contentfwk_objective);
    }

}