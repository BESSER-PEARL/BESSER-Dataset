





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_seff_pc_av_SynchronisationPoint  {






    private List<VariableUsage> variableusages;




    private List<ForkedBehaviour> forkedbehaviours;




    private ForkAction forkaction;


    public pcm_pc_av_seff_pc_av_SynchronisationPoint(
    ) {
        this.variableusages = new ArrayList<>();
        this.forkedbehaviours = new ArrayList<>();
    }

    public pcm_pc_av_seff_pc_av_SynchronisationPoint(
        ArrayList<VariableUsage> variableusages,        ArrayList<ForkedBehaviour> forkedbehaviours    ) {
        this.variableusages = variableusages;
        this.forkedbehaviours = forkedbehaviours;
    }


    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public List<ForkedBehaviour> getForkedbehaviours() {
        return forkedbehaviours;
    }

    public void addForkedbehaviour(Forkedbehaviour forkedbehaviour) {
        this.forkedbehaviours.add(forkedbehaviour);
    }
    public ForkAction getForkaction() {
        return forkaction;
    }

    public void setForkaction(ForkAction forkaction) {
        this.forkaction = forkaction;
    }

}