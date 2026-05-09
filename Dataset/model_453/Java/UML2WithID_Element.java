





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Element  {

    private String ID;





    private UML2WithID_Comment uml2withid_comment;




    private UML2WithID_Relationship uml2withid_relationship;




    private List<UML2WithID_Element> uml2withid_elements;




    private UML2WithID_Element uml2withid_element;




    private List<UML2WithID_Comment> uml2withid_comments;


    public UML2WithID_Element(
        String ID    ) {
        this.ID = ID;
        this.uml2withid_elements = new ArrayList<>();
        this.uml2withid_comments = new ArrayList<>();
    }

    public UML2WithID_Element(
        String ID        ArrayList<UML2WithID_Element> uml2withid_elements,        ArrayList<UML2WithID_Comment> uml2withid_comments    ) {
        this.ID = ID;
        this.uml2withid_elements = uml2withid_elements;
        this.uml2withid_comments = uml2withid_comments;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public UML2WithID_Comment getUml2withid_comment() {
        return uml2withid_comment;
    }

    public void setUml2withid_comment(UML2WithID_Comment uml2withid_comment) {
        this.uml2withid_comment = uml2withid_comment;
    }
    public UML2WithID_Relationship getUml2withid_relationship() {
        return uml2withid_relationship;
    }

    public void setUml2withid_relationship(UML2WithID_Relationship uml2withid_relationship) {
        this.uml2withid_relationship = uml2withid_relationship;
    }
    public List<UML2WithID_Element> getUml2withid_elements() {
        return uml2withid_elements;
    }

    public void addUml2withid_element(Uml2withid_element uml2withid_element) {
        this.uml2withid_elements.add(uml2withid_element);
    }
    public UML2WithID_Element getUml2withid_element() {
        return uml2withid_element;
    }

    public void setUml2withid_element(UML2WithID_Element uml2withid_element) {
        this.uml2withid_element = uml2withid_element;
    }
    public List<UML2WithID_Comment> getUml2withid_comments() {
        return uml2withid_comments;
    }

    public void addUml2withid_comment(Uml2withid_comment uml2withid_comment) {
        this.uml2withid_comments.add(uml2withid_comment);
    }

}