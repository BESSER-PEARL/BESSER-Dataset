





import java.util.List;
import java.util.ArrayList;

public class rell_Conditions  {






    private rell_Relational rell_relational;




    private List<rell_ConditionElement> rell_conditionelements;


    public rell_Conditions(
    ) {
        this.rell_conditionelements = new ArrayList<>();
    }

    public rell_Conditions(
        ArrayList<rell_ConditionElement> rell_conditionelements    ) {
        this.rell_conditionelements = rell_conditionelements;
    }


    public rell_Relational getRell_relational() {
        return rell_relational;
    }

    public void setRell_relational(rell_Relational rell_relational) {
        this.rell_relational = rell_relational;
    }
    public List<rell_ConditionElement> getRell_conditionelements() {
        return rell_conditionelements;
    }

    public void addRell_conditionelement(Rell_conditionelement rell_conditionelement) {
        this.rell_conditionelements.add(rell_conditionelement);
    }

}