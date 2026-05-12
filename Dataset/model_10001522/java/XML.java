





import java.util.List;
import java.util.ArrayList;

public class XML  {

    private String element;
    private String attribute;



    public XML(
        String element,        String attribute    ) {
        this.element = element;
        this.attribute = attribute;
    }


    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}