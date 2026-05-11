





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_SENSINACT  {






    private sensinact_Sensinact sensinact_sensinact;




    private List<sensinact_DSL_CEP_STATEMENT> sensinact_dsl_cep_statements;




    private List<sensinact_DSL_Resource> sensinact_dsl_resources;




    private sensinact_DSL_ECA_STATEMENT sensinact_dsl_eca_statement;


    public sensinact_DSL_SENSINACT(
    ) {
        this.sensinact_dsl_cep_statements = new ArrayList<>();
        this.sensinact_dsl_resources = new ArrayList<>();
    }

    public sensinact_DSL_SENSINACT(
        ArrayList<sensinact_DSL_CEP_STATEMENT> sensinact_dsl_cep_statements,        ArrayList<sensinact_DSL_Resource> sensinact_dsl_resources    ) {
        this.sensinact_dsl_cep_statements = sensinact_dsl_cep_statements;
        this.sensinact_dsl_resources = sensinact_dsl_resources;
    }


    public sensinact_Sensinact getSensinact_sensinact() {
        return sensinact_sensinact;
    }

    public void setSensinact_sensinact(sensinact_Sensinact sensinact_sensinact) {
        this.sensinact_sensinact = sensinact_sensinact;
    }
    public List<sensinact_DSL_CEP_STATEMENT> getSensinact_dsl_cep_statements() {
        return sensinact_dsl_cep_statements;
    }

    public void addSensinact_dsl_cep_statement(Sensinact_dsl_cep_statement sensinact_dsl_cep_statement) {
        this.sensinact_dsl_cep_statements.add(sensinact_dsl_cep_statement);
    }
    public List<sensinact_DSL_Resource> getSensinact_dsl_resources() {
        return sensinact_dsl_resources;
    }

    public void addSensinact_dsl_resource(Sensinact_dsl_resource sensinact_dsl_resource) {
        this.sensinact_dsl_resources.add(sensinact_dsl_resource);
    }
    public sensinact_DSL_ECA_STATEMENT getSensinact_dsl_eca_statement() {
        return sensinact_dsl_eca_statement;
    }

    public void setSensinact_dsl_eca_statement(sensinact_DSL_ECA_STATEMENT sensinact_dsl_eca_statement) {
        this.sensinact_dsl_eca_statement = sensinact_dsl_eca_statement;
    }

}