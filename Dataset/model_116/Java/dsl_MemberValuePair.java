





import java.util.List;
import java.util.ArrayList;

public class dsl_MemberValuePair  {

    private String id;





    private dsl_MemberValuePairs dsl_membervaluepairs;




    private dsl_MemberValue dsl_membervalue;


    public dsl_MemberValuePair(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_MemberValuePairs getDsl_membervaluepairs() {
        return dsl_membervaluepairs;
    }

    public void setDsl_membervaluepairs(dsl_MemberValuePairs dsl_membervaluepairs) {
        this.dsl_membervaluepairs = dsl_membervaluepairs;
    }
    public dsl_MemberValue getDsl_membervalue() {
        return dsl_membervalue;
    }

    public void setDsl_membervalue(dsl_MemberValue dsl_membervalue) {
        this.dsl_membervalue = dsl_membervalue;
    }

}