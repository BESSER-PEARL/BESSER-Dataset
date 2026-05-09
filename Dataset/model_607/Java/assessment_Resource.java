





import java.util.List;
import java.util.ArrayList;

public class assessment_Resource extends Label, Contents, Notes {






    private List<assessment_Snippet> assessment_snippets;




    private assessment_Snippet assessment_snippet;


    public assessment_Resource(
    ) {
        super(
        );
        this.assessment_snippets = new ArrayList<>();
    }

    public assessment_Resource(
        ArrayList<assessment_Snippet> assessment_snippets    ) {
        this.assessment_snippets = assessment_snippets;
    }


    public List<assessment_Snippet> getAssessment_snippets() {
        return assessment_snippets;
    }

    public void addAssessment_snippet(Assessment_snippet assessment_snippet) {
        this.assessment_snippets.add(assessment_snippet);
    }
    public assessment_Snippet getAssessment_snippet() {
        return assessment_snippet;
    }

    public void setAssessment_snippet(assessment_Snippet assessment_snippet) {
        this.assessment_snippet = assessment_snippet;
    }

}