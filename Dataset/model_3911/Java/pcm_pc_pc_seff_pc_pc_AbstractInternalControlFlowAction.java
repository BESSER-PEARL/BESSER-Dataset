





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction extends AbstractAction {






    private List<seff_performance_pc_pc_InfrastructureCall> seff_performance_pc_pc_infrastructurecalls;




    private List<seff_performance_pc_pc_ResourceCall> seff_performance_pc_pc_resourcecalls;




    private List<seff_performance_pc_pc_ParametricResourceDemand> seff_performance_pc_pc_parametricresourcedemands;


    public pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction(
    ) {
        super(
        );
        this.seff_performance_pc_pc_infrastructurecalls = new ArrayList<>();
        this.seff_performance_pc_pc_resourcecalls = new ArrayList<>();
        this.seff_performance_pc_pc_parametricresourcedemands = new ArrayList<>();
    }

    public pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction(
        ArrayList<seff_performance_pc_pc_InfrastructureCall> seff_performance_pc_pc_infrastructurecalls,        ArrayList<seff_performance_pc_pc_ResourceCall> seff_performance_pc_pc_resourcecalls,        ArrayList<seff_performance_pc_pc_ParametricResourceDemand> seff_performance_pc_pc_parametricresourcedemands    ) {
        this.seff_performance_pc_pc_infrastructurecalls = seff_performance_pc_pc_infrastructurecalls;
        this.seff_performance_pc_pc_resourcecalls = seff_performance_pc_pc_resourcecalls;
        this.seff_performance_pc_pc_parametricresourcedemands = seff_performance_pc_pc_parametricresourcedemands;
    }


    public List<seff_performance_pc_pc_InfrastructureCall> getSeff_performance_pc_pc_infrastructurecalls() {
        return seff_performance_pc_pc_infrastructurecalls;
    }

    public void addSeff_performance_pc_pc_infrastructurecall(Seff_performance_pc_pc_infrastructurecall seff_performance_pc_pc_infrastructurecall) {
        this.seff_performance_pc_pc_infrastructurecalls.add(seff_performance_pc_pc_infrastructurecall);
    }
    public List<seff_performance_pc_pc_ResourceCall> getSeff_performance_pc_pc_resourcecalls() {
        return seff_performance_pc_pc_resourcecalls;
    }

    public void addSeff_performance_pc_pc_resourcecall(Seff_performance_pc_pc_resourcecall seff_performance_pc_pc_resourcecall) {
        this.seff_performance_pc_pc_resourcecalls.add(seff_performance_pc_pc_resourcecall);
    }
    public List<seff_performance_pc_pc_ParametricResourceDemand> getSeff_performance_pc_pc_parametricresourcedemands() {
        return seff_performance_pc_pc_parametricresourcedemands;
    }

    public void addSeff_performance_pc_pc_parametricresourcedemand(Seff_performance_pc_pc_parametricresourcedemand seff_performance_pc_pc_parametricresourcedemand) {
        this.seff_performance_pc_pc_parametricresourcedemands.add(seff_performance_pc_pc_parametricresourcedemand);
    }

}