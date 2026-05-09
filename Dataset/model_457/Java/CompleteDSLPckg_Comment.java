





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Comment extends Element {

    private String body;





    private CompleteDSLPckg_Element completedslpckg_element;




    private CompleteDSLPckg_Element completedslpckg_element;




    private List<CompleteDSLPckg_Element> completedslpckg_elements;


    public CompleteDSLPckg_Comment(
        String body    ) {
        super(
        );
        this.body = body;
        this.completedslpckg_elements = new ArrayList<>();
    }

    public CompleteDSLPckg_Comment(
        String body        ArrayList<CompleteDSLPckg_Element> completedslpckg_elements    ) {
        this.body = body;
        this.completedslpckg_elements = completedslpckg_elements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public CompleteDSLPckg_Element getCompletedslpckg_element() {
        return completedslpckg_element;
    }

    public void setCompletedslpckg_element(CompleteDSLPckg_Element completedslpckg_element) {
        this.completedslpckg_element = completedslpckg_element;
    }
    public CompleteDSLPckg_Element getCompletedslpckg_element() {
        return completedslpckg_element;
    }

    public void setCompletedslpckg_element(CompleteDSLPckg_Element completedslpckg_element) {
        this.completedslpckg_element = completedslpckg_element;
    }
    public List<CompleteDSLPckg_Element> getCompletedslpckg_elements() {
        return completedslpckg_elements;
    }

    public void addCompletedslpckg_element(Completedslpckg_element completedslpckg_element) {
        this.completedslpckg_elements.add(completedslpckg_element);
    }

}