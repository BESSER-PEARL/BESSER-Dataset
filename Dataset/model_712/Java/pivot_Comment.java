





import java.util.List;
import java.util.ArrayList;

public class pivot_Comment extends Element {

    private String body;





    private pivot_Element pivot_element;




    private List<pivot_Element> pivot_elements;


    public pivot_Comment(
        String body    ) {
        super(
        );
        this.body = body;
        this.pivot_elements = new ArrayList<>();
    }

    public pivot_Comment(
        String body        ArrayList<pivot_Element> pivot_elements    ) {
        this.body = body;
        this.pivot_elements = pivot_elements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public pivot_Element getPivot_element() {
        return pivot_element;
    }

    public void setPivot_element(pivot_Element pivot_element) {
        this.pivot_element = pivot_element;
    }
    public List<pivot_Element> getPivot_elements() {
        return pivot_elements;
    }

    public void addPivot_element(Pivot_element pivot_element) {
        this.pivot_elements.add(pivot_element);
    }

}