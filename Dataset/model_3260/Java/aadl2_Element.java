





import java.util.List;
import java.util.ArrayList;

public class aadl2_Element  {






    private aadl2_Relationship aadl2_relationship;




    private aadl2_Element aadl2_element;




    private List<aadl2_Element> aadl2_elements;




    private List<aadl2_Comment> aadl2_comments;


    public aadl2_Element(
    ) {
        this.aadl2_elements = new ArrayList<>();
        this.aadl2_comments = new ArrayList<>();
    }

    public aadl2_Element(
        ArrayList<aadl2_Element> aadl2_elements,        ArrayList<aadl2_Comment> aadl2_comments    ) {
        this.aadl2_elements = aadl2_elements;
        this.aadl2_comments = aadl2_comments;
    }


    public aadl2_Relationship getAadl2_relationship() {
        return aadl2_relationship;
    }

    public void setAadl2_relationship(aadl2_Relationship aadl2_relationship) {
        this.aadl2_relationship = aadl2_relationship;
    }
    public aadl2_Element getAadl2_element() {
        return aadl2_element;
    }

    public void setAadl2_element(aadl2_Element aadl2_element) {
        this.aadl2_element = aadl2_element;
    }
    public List<aadl2_Element> getAadl2_elements() {
        return aadl2_elements;
    }

    public void addAadl2_element(Aadl2_element aadl2_element) {
        this.aadl2_elements.add(aadl2_element);
    }
    public List<aadl2_Comment> getAadl2_comments() {
        return aadl2_comments;
    }

    public void addAadl2_comment(Aadl2_comment aadl2_comment) {
        this.aadl2_comments.add(aadl2_comment);
    }

}