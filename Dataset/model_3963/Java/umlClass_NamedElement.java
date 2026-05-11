





import java.util.List;
import java.util.ArrayList;

public class umlClass_NamedElement extends Element {

    private String name;
    private String Archpoint;



    public umlClass_NamedElement(
        String name,        String Archpoint    ) {
        super(
        );
        this.name = name;
        this.Archpoint = Archpoint;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getArchpoint() {
        return Archpoint;
    }

    public void setArchpoint(String Archpoint) {
        this.Archpoint = Archpoint;
    }


}