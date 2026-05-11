





import java.util.List;
import java.util.ArrayList;

public class frontend_core_InlineFeature extends NamedElement {

    private boolean multivalued;



    public frontend_core_InlineFeature(
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