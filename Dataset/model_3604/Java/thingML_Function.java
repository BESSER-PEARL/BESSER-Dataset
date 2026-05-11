





import java.util.List;
import java.util.ArrayList;

public class thingML_Function extends AnnotatedElement, NamedElement {

    private boolean abstract;



    public thingML_Function(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}