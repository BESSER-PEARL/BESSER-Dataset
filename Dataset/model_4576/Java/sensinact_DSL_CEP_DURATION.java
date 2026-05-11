





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_CEP_DURATION  {






    private List<sensinact_EObject> sensinact_eobjects;




    private sensinact_DSL_CEP_AFTER sensinact_dsl_cep_after;




    private sensinact_DSL_CEP_AFTER sensinact_dsl_cep_after;


    public sensinact_DSL_CEP_DURATION(
    ) {
        this.sensinact_eobjects = new ArrayList<>();
    }

    public sensinact_DSL_CEP_DURATION(
        ArrayList<sensinact_EObject> sensinact_eobjects    ) {
        this.sensinact_eobjects = sensinact_eobjects;
    }


    public List<sensinact_EObject> getSensinact_eobjects() {
        return sensinact_eobjects;
    }

    public void addSensinact_eobject(Sensinact_eobject sensinact_eobject) {
        this.sensinact_eobjects.add(sensinact_eobject);
    }
    public sensinact_DSL_CEP_AFTER getSensinact_dsl_cep_after() {
        return sensinact_dsl_cep_after;
    }

    public void setSensinact_dsl_cep_after(sensinact_DSL_CEP_AFTER sensinact_dsl_cep_after) {
        this.sensinact_dsl_cep_after = sensinact_dsl_cep_after;
    }
    public sensinact_DSL_CEP_AFTER getSensinact_dsl_cep_after() {
        return sensinact_dsl_cep_after;
    }

    public void setSensinact_dsl_cep_after(sensinact_DSL_CEP_AFTER sensinact_dsl_cep_after) {
        this.sensinact_dsl_cep_after = sensinact_dsl_cep_after;
    }

}