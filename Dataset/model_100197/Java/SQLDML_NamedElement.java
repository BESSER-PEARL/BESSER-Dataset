





import java.util.List;
import java.util.ArrayList;

public class SQLDML_NamedElement extends LocatedElement {

    private String name;



    public SQLDML_NamedElement(
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