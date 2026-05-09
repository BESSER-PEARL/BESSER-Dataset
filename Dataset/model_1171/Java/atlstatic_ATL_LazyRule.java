





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_LazyRule extends ATL_RuleWithPattern, ATL_StaticRule {

    private String isUnique;



    public atlstatic_ATL_LazyRule(
        String isUnique    ) {
        super(
        );
        this.isUnique = isUnique;
    }


    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }


}