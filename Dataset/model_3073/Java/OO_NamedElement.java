





import java.util.List;
import java.util.ArrayList;

public class OO_NamedElement extends AnnotatedElement {

    private String name;



    public OO_NamedElement(
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