





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Procedure extends AnnotatableElement, NamedElement, TypedElement, CodeBlock {

    private boolean clazz;



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


}