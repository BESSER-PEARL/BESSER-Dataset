





import java.util.List;
import java.util.ArrayList;

public class dbl_Procedure extends LocalScope, TypedElement, NamedElement {

    private boolean clazz;
    private boolean abstract;



    public dbl_Procedure(
        boolean clazz,        boolean abstract    ) {
        super(
        );
        this.clazz = clazz;
        this.abstract = abstract;
    }


    public boolean getClazz() {
        return clazz;
    }

    public void setClazz(boolean clazz) {
        this.clazz = clazz;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}