





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_factoryrules_ChildRule  {

    private String name;





    private factoryrules_Rule factoryrules_rule;


    public gestionmodelosconsultas_factoryrules_ChildRule(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public factoryrules_Rule getFactoryrules_rule() {
        return factoryrules_rule;
    }

    public void setFactoryrules_rule(factoryrules_Rule factoryrules_rule) {
        this.factoryrules_rule = factoryrules_rule;
    }

}