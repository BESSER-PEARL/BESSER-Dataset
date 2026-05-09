





import java.util.List;
import java.util.ArrayList;

public class uma_RoleDescription extends ContentDescription {

    private String skills;
    private String synonyms;
    private String assignmentApproaches;



    public uma_RoleDescription(
        String skills,        String synonyms,        String assignmentApproaches    ) {
        super(
        );
        this.skills = skills;
        this.synonyms = synonyms;
        this.assignmentApproaches = assignmentApproaches;
    }


    public String getSkills() {
        return skills;
    }

    public void setSkills(String skills) {
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


}