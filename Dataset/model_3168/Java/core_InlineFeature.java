





import java.util.List;
import java.util.ArrayList;

public class core_InlineFeature extends NamedElement {

    private boolean multivalued;





    private core_InlineClass core_inlineclass;


    public core_InlineFeature(
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

    public core_InlineClass getCore_inlineclass() {
        return core_inlineclass;
    }

    public void setCore_inlineclass(core_InlineClass core_inlineclass) {
        this.core_inlineclass = core_inlineclass;
    }

}