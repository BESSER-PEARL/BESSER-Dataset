





import java.util.List;
import java.util.ArrayList;

public class Element extends AssessmentElement {






    private Project project;


    public Element(
    ) {
        super(
            String,            name,            String,            description        );
    }



    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }

}