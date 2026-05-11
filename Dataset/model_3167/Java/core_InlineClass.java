





import java.util.List;
import java.util.ArrayList;

public class core_InlineClass extends NamedElement {






    private List<core_InlineFeature> core_inlinefeatures;


    public core_InlineClass(
    ) {
        super(
        );
        this.core_inlinefeatures = new ArrayList<>();
    }

    public core_InlineClass(
        ArrayList<core_InlineFeature> core_inlinefeatures    ) {
        this.core_inlinefeatures = core_inlinefeatures;
    }


    public List<core_InlineFeature> getCore_inlinefeatures() {
        return core_inlinefeatures;
    }

    public void addCore_inlinefeature(Core_inlinefeature core_inlinefeature) {
        this.core_inlinefeatures.add(core_inlinefeature);
    }

}