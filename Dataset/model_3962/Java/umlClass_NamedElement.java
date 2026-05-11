





import java.util.List;
import java.util.ArrayList;

public class umlClass_NamedElement extends Element {

    private String Archpoint;
    private String name;



    public umlClass_NamedElement(
        String Archpoint,        String name    ) {
        super(
        );
        this.Archpoint = Archpoint;
        this.name = name;
    }


    public String getArchpoint() {
        return Archpoint;
    }

    public void setArchpoint(String Archpoint) {
        this.Archpoint = Archpoint;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}