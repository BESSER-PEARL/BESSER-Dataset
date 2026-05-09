





import java.util.List;
import java.util.ArrayList;

public class ATL_LazyMatchedRule extends MatchedRule {

    private String isUnique;



    public ATL_LazyMatchedRule(
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