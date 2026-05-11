





import java.util.List;
import java.util.ArrayList;

public class build_ProvidesPredicate extends BExpression {






    private build_UnitConcernContext build_unitconcerncontext;




    private build_CapabilityPredicate build_capabilitypredicate;


    public build_ProvidesPredicate(
    ) {
        super(
        );
    }



    public build_UnitConcernContext getBuild_unitconcerncontext() {
        return build_unitconcerncontext;
    }

    public void setBuild_unitconcerncontext(build_UnitConcernContext build_unitconcerncontext) {
        this.build_unitconcerncontext = build_unitconcerncontext;
    }
    public build_CapabilityPredicate getBuild_capabilitypredicate() {
        return build_capabilitypredicate;
    }

    public void setBuild_capabilitypredicate(build_CapabilityPredicate build_capabilitypredicate) {
        this.build_capabilitypredicate = build_capabilitypredicate;
    }

}