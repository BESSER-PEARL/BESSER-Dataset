





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction extends AbstractAction {






    private List<seff_performance_pc_av_InfrastructureCall> seff_performance_pc_av_infrastructurecalls;




    private List<seff_performance_pc_av_ResourceCall> seff_performance_pc_av_resourcecalls;




    private List<seff_performance_pc_av_ParametricResourceDemand> seff_performance_pc_av_parametricresourcedemands;


    public pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction(
    ) {
        super(
        );
        this.seff_performance_pc_av_infrastructurecalls = new ArrayList<>();
        this.seff_performance_pc_av_resourcecalls = new ArrayList<>();
        this.seff_performance_pc_av_parametricresourcedemands = new ArrayList<>();
    }

    public pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction(
        ArrayList<seff_performance_pc_av_InfrastructureCall> seff_performance_pc_av_infrastructurecalls,        ArrayList<seff_performance_pc_av_ResourceCall> seff_performance_pc_av_resourcecalls,        ArrayList<seff_performance_pc_av_ParametricResourceDemand> seff_performance_pc_av_parametricresourcedemands    ) {
        this.seff_performance_pc_av_infrastructurecalls = seff_performance_pc_av_infrastructurecalls;
        this.seff_performance_pc_av_resourcecalls = seff_performance_pc_av_resourcecalls;
        this.seff_performance_pc_av_parametricresourcedemands = seff_performance_pc_av_parametricresourcedemands;
    }


    public List<seff_performance_pc_av_InfrastructureCall> getSeff_performance_pc_av_infrastructurecalls() {
        return seff_performance_pc_av_infrastructurecalls;
    }

    public void addSeff_performance_pc_av_infrastructurecall(Seff_performance_pc_av_infrastructurecall seff_performance_pc_av_infrastructurecall) {
        this.seff_performance_pc_av_infrastructurecalls.add(seff_performance_pc_av_infrastructurecall);
    }
    public List<seff_performance_pc_av_ResourceCall> getSeff_performance_pc_av_resourcecalls() {
        return seff_performance_pc_av_resourcecalls;
    }

    public void addSeff_performance_pc_av_resourcecall(Seff_performance_pc_av_resourcecall seff_performance_pc_av_resourcecall) {
        this.seff_performance_pc_av_resourcecalls.add(seff_performance_pc_av_resourcecall);
    }
    public List<seff_performance_pc_av_ParametricResourceDemand> getSeff_performance_pc_av_parametricresourcedemands() {
        return seff_performance_pc_av_parametricresourcedemands;
    }

    public void addSeff_performance_pc_av_parametricresourcedemand(Seff_performance_pc_av_parametricresourcedemand seff_performance_pc_av_parametricresourcedemand) {
        this.seff_performance_pc_av_parametricresourcedemands.add(seff_performance_pc_av_parametricresourcedemand);
    }

}