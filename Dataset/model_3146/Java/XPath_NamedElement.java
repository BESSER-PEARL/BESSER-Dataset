





import java.util.List;
import java.util.ArrayList;

public class XPath_NamedElement extends LocatedElement {

    private String name;



    public XPath_NamedElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}