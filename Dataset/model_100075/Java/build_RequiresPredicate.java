





import java.util.List;
import java.util.ArrayList;

public class build_RequiresPredicate extends BExpression {

    private boolean meta;





    private build_CapabilityPredicate build_capabilitypredicate;


    public build_RequiresPredicate(
        boolean meta    ) {
        super(
        );
        this.meta = meta;
    }


    public boolean getMeta() {
        return meta;
    }

    public void setMeta(boolean meta) {
        this.meta = meta;
    }

    public build_CapabilityPredicate getBuild_capabilitypredicate() {
        return build_capabilitypredicate;
    }

    public void setBuild_capabilitypredicate(build_CapabilityPredicate build_capabilitypredicate) {
        this.build_capabilitypredicate = build_capabilitypredicate;
    }

}