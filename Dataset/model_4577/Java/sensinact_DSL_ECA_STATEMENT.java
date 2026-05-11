





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_ECA_STATEMENT  {






    private List<sensinact_DSL_ElseIfDo> sensinact_dsl_elseifdos;




    private sensinact_DSL_ElseDo sensinact_dsl_elsedo;




    private sensinact_DSL_IfDo sensinact_dsl_ifdo;




    private sensinact_DSL_SENSINACT sensinact_dsl_sensinact;


    public sensinact_DSL_ECA_STATEMENT(
    ) {
        this.sensinact_dsl_elseifdos = new ArrayList<>();
    }

    public sensinact_DSL_ECA_STATEMENT(
        ArrayList<sensinact_DSL_ElseIfDo> sensinact_dsl_elseifdos    ) {
        this.sensinact_dsl_elseifdos = sensinact_dsl_elseifdos;
    }


    public List<sensinact_DSL_ElseIfDo> getSensinact_dsl_elseifdos() {
        return sensinact_dsl_elseifdos;
    }

    public void addSensinact_dsl_elseifdo(Sensinact_dsl_elseifdo sensinact_dsl_elseifdo) {
        this.sensinact_dsl_elseifdos.add(sensinact_dsl_elseifdo);
    }
    public sensinact_DSL_ElseDo getSensinact_dsl_elsedo() {
        return sensinact_dsl_elsedo;
    }

    public void setSensinact_dsl_elsedo(sensinact_DSL_ElseDo sensinact_dsl_elsedo) {
        this.sensinact_dsl_elsedo = sensinact_dsl_elsedo;
    }
    public sensinact_DSL_IfDo getSensinact_dsl_ifdo() {
        return sensinact_dsl_ifdo;
    }

    public void setSensinact_dsl_ifdo(sensinact_DSL_IfDo sensinact_dsl_ifdo) {
        this.sensinact_dsl_ifdo = sensinact_dsl_ifdo;
    }
    public sensinact_DSL_SENSINACT getSensinact_dsl_sensinact() {
        return sensinact_dsl_sensinact;
    }

    public void setSensinact_dsl_sensinact(sensinact_DSL_SENSINACT sensinact_dsl_sensinact) {
        this.sensinact_dsl_sensinact = sensinact_dsl_sensinact;
    }

}