





import java.util.List;
import java.util.ArrayList;

public class build_RequiresPredicate extends BExpression {

    private boolean meta;





    private build_UnitConcernContext build_unitconcerncontext;


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

    public build_UnitConcernContext getBuild_unitconcerncontext() {
        return build_unitconcerncontext;
    }

    public void setBuild_unitconcerncontext(build_UnitConcernContext build_unitconcerncontext) {
        this.build_unitconcerncontext = build_unitconcerncontext;
    }

}