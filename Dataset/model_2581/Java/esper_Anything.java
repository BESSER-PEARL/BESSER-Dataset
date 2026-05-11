





import java.util.List;
import java.util.ArrayList;

public class esper_Anything extends ExtraParenthesisRule {

    private String operator;





    private esper_GroupBy esper_groupby;




    private esper_DefaultMethods esper_defaultmethods;




    private esper_Having esper_having;




    private esper_From esper_from;




    private esper_SingleDefinition esper_singledefinition;


    public esper_Anything(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public esper_GroupBy getEsper_groupby() {
        return esper_groupby;
    }

    public void setEsper_groupby(esper_GroupBy esper_groupby) {
        this.esper_groupby = esper_groupby;
    }
    public esper_DefaultMethods getEsper_defaultmethods() {
        return esper_defaultmethods;
    }

    public void setEsper_defaultmethods(esper_DefaultMethods esper_defaultmethods) {
        this.esper_defaultmethods = esper_defaultmethods;
    }
    public esper_Having getEsper_having() {
        return esper_having;
    }

    public void setEsper_having(esper_Having esper_having) {
        this.esper_having = esper_having;
    }
    public esper_From getEsper_from() {
        return esper_from;
    }

    public void setEsper_from(esper_From esper_from) {
        this.esper_from = esper_from;
    }
    public esper_SingleDefinition getEsper_singledefinition() {
        return esper_singledefinition;
    }

    public void setEsper_singledefinition(esper_SingleDefinition esper_singledefinition) {
        this.esper_singledefinition = esper_singledefinition;
    }

}