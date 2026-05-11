





import java.util.List;
import java.util.ArrayList;

public class ram_StructuralFeature extends TypedElement {

    private boolean static;



    public ram_StructuralFeature(
        boolean static    ) {
        super(
        );
        this.static = static;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}