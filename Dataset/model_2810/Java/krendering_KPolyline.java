





import java.util.List;
import java.util.ArrayList;

public class krendering_KPolyline extends KContainerRendering {






    private List<krendering_KPosition> krendering_kpositions;


    public krendering_KPolyline(
    ) {
        super(
        );
        this.krendering_kpositions = new ArrayList<>();
    }

    public krendering_KPolyline(
        ArrayList<krendering_KPosition> krendering_kpositions    ) {
        this.krendering_kpositions = krendering_kpositions;
    }


    public List<krendering_KPosition> getKrendering_kpositions() {
        return krendering_kpositions;
    }

    public void addKrendering_kposition(Krendering_kposition krendering_kposition) {
        this.krendering_kpositions.add(krendering_kposition);
    }

}