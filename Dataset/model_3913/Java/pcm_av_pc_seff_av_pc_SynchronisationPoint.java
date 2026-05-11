





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_seff_av_pc_SynchronisationPoint  {






    private ForkAction forkaction;




    private List<VariableUsage> variableusages;




    private List<ForkedBehaviour> forkedbehaviours;


    public pcm_av_pc_seff_av_pc_SynchronisationPoint(
    ) {
        this.variableusages = new ArrayList<>();
        this.forkedbehaviours = new ArrayList<>();
    }

    public pcm_av_pc_seff_av_pc_SynchronisationPoint(
        ArrayList<VariableUsage> variableusages,        ArrayList<ForkedBehaviour> forkedbehaviours    ) {
        this.variableusages = variableusages;
        this.forkedbehaviours = forkedbehaviours;
    }


    public ForkAction getForkaction() {
        return forkaction;
    }

    public void setForkaction(ForkAction forkaction) {
        this.forkaction = forkaction;
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

}