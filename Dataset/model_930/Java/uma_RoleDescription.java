





import java.util.List;
import java.util.ArrayList;

public class uma_RoleDescription extends ContentDescription {

    private String synonyms;
    private String assignmentApproaches;
    private String skills;



    public uma_RoleDescription(
        String synonyms,        String assignmentApproaches,        String skills    ) {
        super(
        );
        this.synonyms = synonyms;
        this.assignmentApproaches = assignmentApproaches;
        this.skills = skills;
    }


    public String getSynonyms() {
        return synonyms;
    }

    public void setSynonyms(String synonyms) {
        this.synonyms = synonyms;
    }
    public String getAssignmentapproaches() {
        return assignmentApproaches;
    }

    public void setAssignmentapproaches(String assignmentApproaches) {
        this.assignmentApproaches = assignmentApproaches;
    }
    public String getSkills() {
        return skills;
    }

    public void setSkills(String skills) {
        this.skills = skills;
    }


}