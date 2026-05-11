





import java.util.List;
import java.util.ArrayList;

public class relational_SQLObject extends ENamedElement {

    private String label;
    private String description;





    private relational_Comment relational_comment;




    private List<relational_Comment> relational_comments;


    public relational_SQLObject(
        String label,        String description    ) {
        super(
        );
        this.label = label;
        this.description = description;
        this.relational_comments = new ArrayList<>();
    }

    public relational_SQLObject(
        String label,        String description        ArrayList<relational_Comment> relational_comments    ) {
        this.label = label;
        this.description = description;
        this.relational_comments = relational_comments;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public relational_Comment getRelational_comment() {
        return relational_comment;
    }

    public void setRelational_comment(relational_Comment relational_comment) {
        this.relational_comment = relational_comment;
    }
    public List<relational_Comment> getRelational_comments() {
        return relational_comments;
    }

    public void addRelational_comment(Relational_comment relational_comment) {
        this.relational_comments.add(relational_comment);
    }

}