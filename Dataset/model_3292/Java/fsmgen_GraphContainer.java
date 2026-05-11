





import java.util.List;
import java.util.ArrayList;

public class fsmgen_GraphContainer extends FSMGenElement {

    private boolean initializedCommonData;
    private boolean initializedChainHeads;
    private boolean initializedTriggersInStates;





    private fsmgen_ModelComponent fsmgen_modelcomponent;


    public fsmgen_GraphContainer(
        boolean initializedCommonData,        boolean initializedChainHeads,        boolean initializedTriggersInStates    ) {
        super(
        );
        this.initializedCommonData = initializedCommonData;
        this.initializedChainHeads = initializedChainHeads;
        this.initializedTriggersInStates = initializedTriggersInStates;
    }


    public boolean getInitializedcommondata() {
        return initializedCommonData;
    }

    public void setInitializedcommondata(boolean initializedCommonData) {
        this.initializedCommonData = initializedCommonData;
    }
    public boolean getInitializedchainheads() {
        return initializedChainHeads;
    }

    public void setInitializedchainheads(boolean initializedChainHeads) {
        this.initializedChainHeads = initializedChainHeads;
    }
    public boolean getInitializedtriggersinstates() {
        return initializedTriggersInStates;
    }

    public void setInitializedtriggersinstates(boolean initializedTriggersInStates) {
        this.initializedTriggersInStates = initializedTriggersInStates;
    }

    public fsmgen_ModelComponent getFsmgen_modelcomponent() {
        return fsmgen_modelcomponent;
    }

    public void setFsmgen_modelcomponent(fsmgen_ModelComponent fsmgen_modelcomponent) {
        this.fsmgen_modelcomponent = fsmgen_modelcomponent;
    }

}