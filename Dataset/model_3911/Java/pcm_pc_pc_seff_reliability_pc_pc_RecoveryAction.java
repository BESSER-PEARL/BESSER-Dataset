





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction extends AbstractInternalControlFlowAction {






    private List<seff_reliability_pc_pc_RecoveryActionBehaviour> seff_reliability_pc_pc_recoveryactionbehaviours;




    private seff_reliability_pc_pc_RecoveryActionBehaviour seff_reliability_pc_pc_recoveryactionbehaviour;


    public pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(
    ) {
        super(
        );
        this.seff_reliability_pc_pc_recoveryactionbehaviours = new ArrayList<>();
    }

    public pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(
        ArrayList<seff_reliability_pc_pc_RecoveryActionBehaviour> seff_reliability_pc_pc_recoveryactionbehaviours    ) {
        this.seff_reliability_pc_pc_recoveryactionbehaviours = seff_reliability_pc_pc_recoveryactionbehaviours;
    }


    public List<seff_reliability_pc_pc_RecoveryActionBehaviour> getSeff_reliability_pc_pc_recoveryactionbehaviours() {
        return seff_reliability_pc_pc_recoveryactionbehaviours;
    }

    public void addSeff_reliability_pc_pc_recoveryactionbehaviour(Seff_reliability_pc_pc_recoveryactionbehaviour seff_reliability_pc_pc_recoveryactionbehaviour) {
        this.seff_reliability_pc_pc_recoveryactionbehaviours.add(seff_reliability_pc_pc_recoveryactionbehaviour);
    }
    public seff_reliability_pc_pc_RecoveryActionBehaviour getSeff_reliability_pc_pc_recoveryactionbehaviour() {
        return seff_reliability_pc_pc_recoveryactionbehaviour;
    }

    public void setSeff_reliability_pc_pc_recoveryactionbehaviour(seff_reliability_pc_pc_RecoveryActionBehaviour seff_reliability_pc_pc_recoveryactionbehaviour) {
        this.seff_reliability_pc_pc_recoveryactionbehaviour = seff_reliability_pc_pc_recoveryactionbehaviour;
    }

}