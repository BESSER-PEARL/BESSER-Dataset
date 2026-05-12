





import java.util.List;
import java.util.ArrayList;

public class requirements_editor_SimpleDependency extends Dependency {

    private String comment;





    private requirements_editor_Requirement requirements_editor_requirement;


    public requirements_editor_SimpleDependency(
        String comment    ) {
        super(
        );
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public requirements_editor_Requirement getRequirements_editor_requirement() {
        return requirements_editor_requirement;
    }

    public void setRequirements_editor_requirement(requirements_editor_Requirement requirements_editor_requirement) {
        this.requirements_editor_requirement = requirements_editor_requirement;
    }

}