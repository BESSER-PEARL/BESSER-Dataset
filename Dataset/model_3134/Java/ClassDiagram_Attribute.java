





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Attribute extends StructuralFeature {

    private boolean multivalued;



    public ClassDiagram_Attribute(
        boolean multivalued    ) {
        super(
        );
        this.multivalued = multivalued;
    }


    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }


}