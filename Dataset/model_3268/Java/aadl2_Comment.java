





import java.util.List;
import java.util.ArrayList;

public class aadl2_Comment extends Element {

    private String body;





    private aadl2_Element aadl2_element;


    public aadl2_Comment(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public aadl2_Element getAadl2_element() {
        return aadl2_element;
    }

    public void setAadl2_element(aadl2_Element aadl2_element) {
        this.aadl2_element = aadl2_element;
    }

}