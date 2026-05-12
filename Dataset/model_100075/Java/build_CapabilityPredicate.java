





import java.util.List;
import java.util.ArrayList;

public class build_CapabilityPredicate extends BExpression {

    private String versionRange;





    private build_ProvidesPredicate build_providespredicate;


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

    public build_ProvidesPredicate getBuild_providespredicate() {
        return build_providespredicate;
    }

    public void setBuild_providespredicate(build_ProvidesPredicate build_providespredicate) {
        this.build_providespredicate = build_providespredicate;
    }

}