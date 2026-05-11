





import java.util.List;
import java.util.ArrayList;

public class behavior_NamedElement extends Element {

    private boolean Archpoint;
    private String name;



    public behavior_NamedElement(
        boolean Archpoint,        String name    ) {
        super(
        );
        this.Archpoint = Archpoint;
        this.name = name;
    }


    public boolean getArchpoint() {
        return Archpoint;
    }

    public void setArchpoint(boolean Archpoint) {
        this.Archpoint = Archpoint;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}