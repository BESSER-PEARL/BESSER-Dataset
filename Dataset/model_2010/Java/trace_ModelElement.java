





import java.util.List;
import java.util.ArrayList;

public class trace_ModelElement extends TraceElement {

    private String element_id;



    public trace_ModelElement(
        String element_id    ) {
        super(
        );
        this.element_id = element_id;
    }


    public String getElement_id() {
        return element_id;
    }

    public void setElement_id(String element_id) {
        this.element_id = element_id;
    }


}