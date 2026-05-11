





import java.util.List;
import java.util.ArrayList;

public class dbl_Procedure extends TypedElement, AnnotatableElement, NamedElement, CodeBlock {

    private boolean clazz;





    private dbl_Module dbl_module;


    public dbl_Procedure(
        boolean clazz    ) {
        super(
        );
        this.clazz = clazz;
    }


    public boolean getClazz() {
        return clazz;
    }

    public void setClazz(boolean clazz) {
        this.clazz = clazz;
    }

    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }

}