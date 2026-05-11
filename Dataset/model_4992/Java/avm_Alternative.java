





import java.util.List;
import java.util.ArrayList;

public class avm_Alternative extends DesignSpaceContainer {






    private List<avm_ValueFlowMux> avm_valueflowmuxs;


    public avm_Alternative(
    ) {
        super(
        );
        this.avm_valueflowmuxs = new ArrayList<>();
    }

    public avm_Alternative(
        ArrayList<avm_ValueFlowMux> avm_valueflowmuxs    ) {
        this.avm_valueflowmuxs = avm_valueflowmuxs;
    }


    public List<avm_ValueFlowMux> getAvm_valueflowmuxs() {
        return avm_valueflowmuxs;
    }

    public void addAvm_valueflowmux(Avm_valueflowmux avm_valueflowmux) {
        this.avm_valueflowmuxs.add(avm_valueflowmux);
    }

}