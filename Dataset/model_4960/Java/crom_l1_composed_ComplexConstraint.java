





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_ComplexConstraint extends Constraint {

    private String expression;





    private List<crom_l1_composed_AbstractRole> crom_l1_composed_abstractroles;


    public crom_l1_composed_ComplexConstraint(
        String expression    ) {
        super(
        );
        this.expression = expression;
        this.crom_l1_composed_abstractroles = new ArrayList<>();
    }

    public crom_l1_composed_ComplexConstraint(
        String expression        ArrayList<crom_l1_composed_AbstractRole> crom_l1_composed_abstractroles    ) {
        this.expression = expression;
        this.crom_l1_composed_abstractroles = crom_l1_composed_abstractroles;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public List<crom_l1_composed_AbstractRole> getCrom_l1_composed_abstractroles() {
        return crom_l1_composed_abstractroles;
    }

    public void addCrom_l1_composed_abstractrole(Crom_l1_composed_abstractrole crom_l1_composed_abstractrole) {
        this.crom_l1_composed_abstractroles.add(crom_l1_composed_abstractrole);
    }

}