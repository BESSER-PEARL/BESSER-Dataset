





import java.util.List;
import java.util.ArrayList;

public class brmodel_Model  {






    private List<brmodel_Rule> brmodel_rules;


    public brmodel_Model(
    ) {
        this.brmodel_rules = new ArrayList<>();
    }

    public brmodel_Model(
        ArrayList<brmodel_Rule> brmodel_rules    ) {
        this.brmodel_rules = brmodel_rules;
    }


    public List<brmodel_Rule> getBrmodel_rules() {
        return brmodel_rules;
    }

    public void addBrmodel_rule(Brmodel_rule brmodel_rule) {
        this.brmodel_rules.add(brmodel_rule);
    }

}