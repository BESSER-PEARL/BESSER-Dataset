





import java.util.List;
import java.util.ArrayList;

public class plSql_PragmaRestrictReferences extends Pragma {

    private String restrictions;



    public plSql_PragmaRestrictReferences(
        String restrictions    ) {
        super(
        );
        this.restrictions = restrictions;
    }


    public String getRestrictions() {
        return restrictions;
    }

    public void setRestrictions(String restrictions) {
        this.restrictions = restrictions;
    }


}