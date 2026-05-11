





import java.util.List;
import java.util.ArrayList;

public class cmof_Comment extends Element {

    private String body;





    private cmof_Element cmof_element;




    private List<cmof_Element> cmof_elements;


    public cmof_Comment(
        String body    ) {
        super(
        );
        this.body = body;
        this.cmof_elements = new ArrayList<>();
    }

    public cmof_Comment(
        String body        ArrayList<cmof_Element> cmof_elements    ) {
        this.body = body;
        this.cmof_elements = cmof_elements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public cmof_Element getCmof_element() {
        return cmof_element;
    }

    public void setCmof_element(cmof_Element cmof_element) {
        this.cmof_element = cmof_element;
    }
    public List<cmof_Element> getCmof_elements() {
        return cmof_elements;
    }

    public void addCmof_element(Cmof_element cmof_element) {
        this.cmof_elements.add(cmof_element);
    }

}