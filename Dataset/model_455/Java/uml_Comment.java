





import java.util.List;
import java.util.ArrayList;

public class uml_Comment extends Element {

    private String body;





    private uml_Element uml_element;




    private List<uml_Element> uml_elements;


    public uml_Comment(
        String body    ) {
        super(
        );
        this.body = body;
        this.uml_elements = new ArrayList<>();
    }

    public uml_Comment(
        String body        ArrayList<uml_Element> uml_elements    ) {
        this.body = body;
        this.uml_elements = uml_elements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public uml_Element getUml_element() {
        return uml_element;
    }

    public void setUml_element(uml_Element uml_element) {
        this.uml_element = uml_element;
    }
    public List<uml_Element> getUml_elements() {
        return uml_elements;
    }

    public void addUml_element(Uml_element uml_element) {
        this.uml_elements.add(uml_element);
    }

}