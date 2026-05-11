





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Procedure extends AnnotatableElement, CodeBlock, TypedElement, NamedElement {

    private boolean clazz;





    private odemcustom_Module odemcustom_module;


    public odemcustom_Procedure(
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

    public odemcustom_Module getOdemcustom_module() {
        return odemcustom_module;
    }

    public void setOdemcustom_module(odemcustom_Module odemcustom_module) {
        this.odemcustom_module = odemcustom_module;
    }

}