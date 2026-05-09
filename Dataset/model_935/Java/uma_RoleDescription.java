





import java.util.List;
import java.util.ArrayList;

public class uma_RoleDescription extends ContentDescription {

    private String skills;
    private String assignmentApproaches;
    private String synonyms;



    public uma_RoleDescription(
        String skills,        String assignmentApproaches,        String synonyms    ) {
        super(
        );
        this.skills = skills;
        this.assignmentApproaches = assignmentApproaches;
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
    public String getSynonyms() {
        return synonyms;
    }

    public void setSynonyms(String synonyms) {
        this.synonyms = synonyms;
    }


}