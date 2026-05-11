





import java.util.List;
import java.util.ArrayList;

public class persistence_StaticPathElement extends PathElement {

    private String element;



    public persistence_StaticPathElement(
        String element    ) {
        super(
        );
        this.element = element;
    }


    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }


}