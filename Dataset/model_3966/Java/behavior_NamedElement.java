





import java.util.List;
import java.util.ArrayList;

public class behavior_NamedElement extends Element {

    private String name;
    private boolean Archpoint;



    public behavior_NamedElement(
        String name,        boolean Archpoint    ) {
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
    public boolean getArchpoint() {
        return Archpoint;
    }

    public void setArchpoint(boolean Archpoint) {
        this.Archpoint = Archpoint;
    }


}