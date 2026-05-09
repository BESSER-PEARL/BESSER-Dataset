





import java.util.List;
import java.util.ArrayList;

public class dsl_MemberValueArrayInitializer  {






    private List<dsl_MemberValue> dsl_membervalues;




    private dsl_MemberValue dsl_membervalue;


    public dsl_MemberValueArrayInitializer(
    ) {
        this.dsl_membervalues = new ArrayList<>();
    }

    public dsl_MemberValueArrayInitializer(
        ArrayList<dsl_MemberValue> dsl_membervalues    ) {
        this.dsl_membervalues = dsl_membervalues;
    }


    public List<dsl_MemberValue> getDsl_membervalues() {
        return dsl_membervalues;
    }

    public void addDsl_membervalue(Dsl_membervalue dsl_membervalue) {
        this.dsl_membervalues.add(dsl_membervalue);
    }
    public dsl_MemberValue getDsl_membervalue() {
        return dsl_membervalue;
    }

    public void setDsl_membervalue(dsl_MemberValue dsl_membervalue) {
        this.dsl_membervalue = dsl_membervalue;
    }

}