





import java.util.List;
import java.util.ArrayList;

public class types_Declaration extends NamedElement, AnnotatableElement, MetaComposite {

    private boolean static;
    private String id;





    private types_Package types_package;


    public types_Declaration(
        boolean static,        String id    ) {
        super(
        );
        this.static = static;
        this.id = id;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public types_Package getTypes_package() {
        return types_package;
    }

    public void setTypes_package(types_Package types_package) {
        this.types_package = types_package;
    }

}