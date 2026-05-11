





import java.util.List;
import java.util.ArrayList;

public class build_CapabilityPredicate extends BExpression {

    private String versionRange;





    private build_RequiresPredicate build_requirespredicate;




    private build_UnitConcernContext build_unitconcerncontext;




    private build_InputPredicate build_inputpredicate;


    public build_CapabilityPredicate(
        String versionRange    ) {
        super(
        );
        this.versionRange = versionRange;
    }


    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }

    public build_RequiresPredicate getBuild_requirespredicate() {
        return build_requirespredicate;
    }

    public void setBuild_requirespredicate(build_RequiresPredicate build_requirespredicate) {
        this.build_requirespredicate = build_requirespredicate;
    }
    public build_UnitConcernContext getBuild_unitconcerncontext() {
        return build_unitconcerncontext;
    }

    public void setBuild_unitconcerncontext(build_UnitConcernContext build_unitconcerncontext) {
        this.build_unitconcerncontext = build_unitconcerncontext;
    }
    public build_InputPredicate getBuild_inputpredicate() {
        return build_inputpredicate;
    }

    public void setBuild_inputpredicate(build_InputPredicate build_inputpredicate) {
        this.build_inputpredicate = build_inputpredicate;
    }

}