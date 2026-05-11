





import java.util.List;
import java.util.ArrayList;

public class krendering_KContainerRendering extends KRendering {






    private List<krendering_KRendering> krendering_krenderings;




    private krendering_KRendering krendering_krendering;


    public krendering_KContainerRendering(
    ) {
        super(
        );
        this.krendering_krenderings = new ArrayList<>();
    }

    public krendering_KContainerRendering(
        ArrayList<krendering_KRendering> krendering_krenderings    ) {
        this.krendering_krenderings = krendering_krenderings;
    }


    public List<krendering_KRendering> getKrendering_krenderings() {
        return krendering_krenderings;
    }

    public void addKrendering_krendering(Krendering_krendering krendering_krendering) {
        this.krendering_krenderings.add(krendering_krendering);
    }
    public krendering_KRendering getKrendering_krendering() {
        return krendering_krendering;
    }

    public void setKrendering_krendering(krendering_KRendering krendering_krendering) {
        this.krendering_krendering = krendering_krendering;
    }

}