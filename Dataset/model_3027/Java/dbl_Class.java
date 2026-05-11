





import java.util.List;
import java.util.ArrayList;

public class dbl_Class extends Construct, ConstructiveExtensionAtContentExtensionPoint, AnnotateableElement, Concept, NamedElement, Type {

    private boolean active;





    private dbl_Module dbl_module;


    public dbl_Class(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }

}