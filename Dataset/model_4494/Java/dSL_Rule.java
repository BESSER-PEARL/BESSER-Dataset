





import java.util.List;
import java.util.ArrayList;

public class dSL_Rule  {






    private dSL_Specification dsl_specification;




    private dSL_ConditionList dsl_conditionlist;


    public dSL_Rule(
    ) {
    }



    public dSL_Specification getDsl_specification() {
        return dsl_specification;
    }

    public void setDsl_specification(dSL_Specification dsl_specification) {
        this.dsl_specification = dsl_specification;
    }
    public dSL_ConditionList getDsl_conditionlist() {
        return dsl_conditionlist;
    }

    public void setDsl_conditionlist(dSL_ConditionList dsl_conditionlist) {
        this.dsl_conditionlist = dsl_conditionlist;
    }

}