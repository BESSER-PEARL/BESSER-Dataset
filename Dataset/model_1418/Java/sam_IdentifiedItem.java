





import java.util.List;
import java.util.ArrayList;

public class sam_IdentifiedItem extends EModelElement {

    private String requirements;
    private String comment;



    public sam_IdentifiedItem(
        String requirements,        String comment    ) {
        super(
        );
        this.requirements = requirements;
        this.comment = comment;
    }


    public String getRequirements() {
        return requirements;
    }

    public void setRequirements(String requirements) {
        this.requirements = requirements;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}