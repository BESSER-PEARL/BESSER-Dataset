





import java.util.List;
import java.util.ArrayList;

public class uma_RoleDescription extends ContentDescription {

    private String synonyms;
    private String skills;
    private String assignmentApproaches;



    public uma_RoleDescription(
        String synonyms,        String skills,        String assignmentApproaches    ) {
        super(
        );
        this.synonyms = synonyms;
        this.skills = skills;
        this.assignmentApproaches = assignmentApproaches;
    }


    public String getSynonyms() {
        return synonyms;
    }

    public void setSynonyms(String synonyms) {
        this.synonyms = synonyms;
    }
    public String getSkills() {
        return skills;
    }

    public void setSkills(String skills) {
        this.skills = skills;
    }
    public String getAssignmentapproaches() {
        return assignmentApproaches;
    }

    public void setAssignmentapproaches(String assignmentApproaches) {
        this.assignmentApproaches = assignmentApproaches;
    }


}