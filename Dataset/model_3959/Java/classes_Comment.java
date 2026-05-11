





import java.util.List;
import java.util.ArrayList;

public class classes_Comment  {

    private String body;





    private List<classes_Element> classes_elements;




    private classes_Element classes_element;


    public classes_Comment(
        String body    ) {
        this.body = body;
        this.classes_elements = new ArrayList<>();
    }

    public classes_Comment(
        String body        ArrayList<classes_Element> classes_elements    ) {
        this.body = body;
        this.classes_elements = classes_elements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<classes_Element> getClasses_elements() {
        return classes_elements;
    }

    public void addClasses_element(Classes_element classes_element) {
        this.classes_elements.add(classes_element);
    }
    public classes_Element getClasses_element() {
        return classes_element;
    }

    public void setClasses_element(classes_Element classes_element) {
        this.classes_element = classes_element;
    }

}