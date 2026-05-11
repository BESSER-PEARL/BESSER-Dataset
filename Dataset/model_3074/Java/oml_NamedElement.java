





import java.util.List;
import java.util.ArrayList;

public class oml_NamedElement extends AnnotatedElement {

    private String name;



    public oml_NamedElement(
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