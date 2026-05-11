





import java.util.List;
import java.util.ArrayList;

public class avm_SimpleFormula extends Formula {

    private String Operation;





    private List<avm_ValueNode> avm_valuenodes;


    public avm_SimpleFormula(
        String Operation    ) {
        super(
        );
        this.Operation = Operation;
        this.avm_valuenodes = new ArrayList<>();
    }

    public avm_SimpleFormula(
        String Operation        ArrayList<avm_ValueNode> avm_valuenodes    ) {
        this.Operation = Operation;
        this.avm_valuenodes = avm_valuenodes;
    }

    public String getOperation() {
        return Operation;
    }

    public void setOperation(String Operation) {
        this.Operation = Operation;
    }

    public List<avm_ValueNode> getAvm_valuenodes() {
        return avm_valuenodes;
    }

    public void addAvm_valuenode(Avm_valuenode avm_valuenode) {
        this.avm_valuenodes.add(avm_valuenode);
    }

}