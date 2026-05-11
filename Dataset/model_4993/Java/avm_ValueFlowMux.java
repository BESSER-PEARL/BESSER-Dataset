





import java.util.List;
import java.util.ArrayList;

public class avm_ValueFlowMux extends ValueNode {






    private avm_Alternative avm_alternative;




    private List<avm_ValueNode> avm_valuenodes;


    public avm_ValueFlowMux(
    ) {
        super(
        );
        this.avm_valuenodes = new ArrayList<>();
    }

    public avm_ValueFlowMux(
        ArrayList<avm_ValueNode> avm_valuenodes    ) {
        this.avm_valuenodes = avm_valuenodes;
    }


    public avm_Alternative getAvm_alternative() {
        return avm_alternative;
    }

    public void setAvm_alternative(avm_Alternative avm_alternative) {
        this.avm_alternative = avm_alternative;
    }
    public List<avm_ValueNode> getAvm_valuenodes() {
        return avm_valuenodes;
    }

    public void addAvm_valuenode(Avm_valuenode avm_valuenode) {
        this.avm_valuenodes.add(avm_valuenode);
    }

}