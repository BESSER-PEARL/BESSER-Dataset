





import java.util.List;
import java.util.ArrayList;

public class express_rules_GlobalRule extends core_AlgorithmScope, core_SchemaElement {






    private List<Extent> extents;


    public express_rules_GlobalRule(
    ) {
        super(
        );
        this.extents = new ArrayList<>();
    }

    public express_rules_GlobalRule(
        ArrayList<Extent> extents    ) {
        this.extents = extents;
    }


    public List<Extent> getExtents() {
        return extents;
    }

    public void addExtent(Extent extent) {
        this.extents.add(extent);
    }

}