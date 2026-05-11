





import java.util.List;
import java.util.ArrayList;

public class pcm_av_seff_av_SynchronisationPoint  {






    private List<ForkedBehaviour> forkedbehaviours;




    private ForkAction forkaction;




    private List<VariableUsage> variableusages;


    public pcm_av_seff_av_SynchronisationPoint(
    ) {
        this.forkedbehaviours = new ArrayList<>();
        this.variableusages = new ArrayList<>();
    }

    public pcm_av_seff_av_SynchronisationPoint(
        ArrayList<ForkedBehaviour> forkedbehaviours,        ArrayList<VariableUsage> variableusages    ) {
        this.forkedbehaviours = forkedbehaviours;
        this.variableusages = variableusages;
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
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }

}