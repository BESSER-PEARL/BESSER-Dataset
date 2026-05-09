





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Element extends UMLBase {

    private String ownedElement;
    private String owner;
    private String href;





    private List<UMLModel_Comment> umlmodel_comments;


    public UMLModel_Element(
        String ownedElement,        String owner,        String href    ) {
        super(
        );
        this.ownedElement = ownedElement;
        this.owner = owner;
        this.href = href;
        this.umlmodel_comments = new ArrayList<>();
    }

    public UMLModel_Element(
        String ownedElement,        String owner,        String href        ArrayList<UMLModel_Comment> umlmodel_comments    ) {
        this.ownedElement = ownedElement;
        this.owner = owner;
        this.href = href;
        this.umlmodel_comments = umlmodel_comments;
    }

    public String getOwnedelement() {
        return ownedElement;
    }

    public void setOwnedelement(String ownedElement) {
        this.ownedElement = ownedElement;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }

    public List<UMLModel_Comment> getUmlmodel_comments() {
        return umlmodel_comments;
    }

    public void addUmlmodel_comment(Umlmodel_comment umlmodel_comment) {
        this.umlmodel_comments.add(umlmodel_comment);
    }

}