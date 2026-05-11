





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_factoryrules_Rule  {

    private String name;





    private factoryrules_RulesFactory factoryrules_rulesfactory;




    private List<factoryrules_ChildRule> factoryrules_childrules;


    public gestionmodelosconsultas_factoryrules_Rule(
        String name    ) {
        this.name = name;
        this.factoryrules_childrules = new ArrayList<>();
    }

    public gestionmodelosconsultas_factoryrules_Rule(
        String name        ArrayList<factoryrules_ChildRule> factoryrules_childrules    ) {
        this.name = name;
        this.factoryrules_childrules = factoryrules_childrules;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public factoryrules_RulesFactory getFactoryrules_rulesfactory() {
        return factoryrules_rulesfactory;
    }

    public void setFactoryrules_rulesfactory(factoryrules_RulesFactory factoryrules_rulesfactory) {
        this.factoryrules_rulesfactory = factoryrules_rulesfactory;
    }
    public List<factoryrules_ChildRule> getFactoryrules_childrules() {
        return factoryrules_childrules;
    }

    public void addFactoryrules_childrule(Factoryrules_childrule factoryrules_childrule) {
        this.factoryrules_childrules.add(factoryrules_childrule);
    }

}