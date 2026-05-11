





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_On  {






    private sensinact_DSL_SENSINACT sensinact_dsl_sensinact;




    private List<sensinact_DSL_REF_CONDITION> sensinact_dsl_ref_conditions;


    public sensinact_DSL_On(
    ) {
        this.sensinact_dsl_ref_conditions = new ArrayList<>();
    }

    public sensinact_DSL_On(
        ArrayList<sensinact_DSL_REF_CONDITION> sensinact_dsl_ref_conditions    ) {
        this.sensinact_dsl_ref_conditions = sensinact_dsl_ref_conditions;
    }


    public sensinact_DSL_SENSINACT getSensinact_dsl_sensinact() {
        return sensinact_dsl_sensinact;
    }

    public void setSensinact_dsl_sensinact(sensinact_DSL_SENSINACT sensinact_dsl_sensinact) {
        this.sensinact_dsl_sensinact = sensinact_dsl_sensinact;
    }
    public List<sensinact_DSL_REF_CONDITION> getSensinact_dsl_ref_conditions() {
        return sensinact_dsl_ref_conditions;
    }

    public void addSensinact_dsl_ref_condition(Sensinact_dsl_ref_condition sensinact_dsl_ref_condition) {
        this.sensinact_dsl_ref_conditions.add(sensinact_dsl_ref_condition);
    }

}