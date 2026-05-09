





import java.util.List;
import java.util.ArrayList;

public class sam_IdentifiedItem extends EModelElement {

    private String comment;
    private String requirements;



    public sam_IdentifiedItem(
        String comment,        String requirements    ) {
        super(
        );
        this.comment = comment;
        this.requirements = requirements;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getRequirements() {
        return requirements;
    }

    public void setRequirements(String requirements) {
        this.requirements = requirements;
    }


}