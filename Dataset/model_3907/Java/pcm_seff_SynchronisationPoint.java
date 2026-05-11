





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_SynchronisationPoint  {






    private List<ForkedBehaviour> forkedbehaviours;


    public pcm_seff_SynchronisationPoint(
    ) {
        this.forkedbehaviours = new ArrayList<>();
    }

    public pcm_seff_SynchronisationPoint(
        ArrayList<ForkedBehaviour> forkedbehaviours    ) {
        this.forkedbehaviours = forkedbehaviours;
    }


    public List<ForkedBehaviour> getForkedbehaviours() {
        return forkedbehaviours;
    }

    public void addForkedbehaviour(Forkedbehaviour forkedbehaviour) {
        this.forkedbehaviours.add(forkedbehaviour);
    }

}