





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_seff_av_av_SynchronisationPoint  {






    private List<ForkedBehaviour> forkedbehaviours;




    private ForkAction forkaction;


    public pcm_av_av_seff_av_av_SynchronisationPoint(
    ) {
        this.forkedbehaviours = new ArrayList<>();
    }

    public pcm_av_av_seff_av_av_SynchronisationPoint(
        ArrayList<ForkedBehaviour> forkedbehaviours    ) {
        this.forkedbehaviours = forkedbehaviours;
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