





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_LazyRule extends ATL_StaticRule, ATL_RuleWithPattern {

    private String isUnique;



    public atlext_ATL_LazyRule(
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