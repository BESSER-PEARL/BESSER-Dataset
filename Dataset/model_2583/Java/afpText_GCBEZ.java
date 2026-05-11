





import java.util.List;
import java.util.ArrayList;

public class afpText_GCBEZ extends triplet {






    private List<afpText_GCBEZRG> afptext_gcbezrgs;


    public afpText_GCBEZ(
    ) {
        super(
        );
        this.afptext_gcbezrgs = new ArrayList<>();
    }

    public afpText_GCBEZ(
        ArrayList<afpText_GCBEZRG> afptext_gcbezrgs    ) {
        this.afptext_gcbezrgs = afptext_gcbezrgs;
    }


    public List<afpText_GCBEZRG> getAfptext_gcbezrgs() {
        return afptext_gcbezrgs;
    }

    public void addAfptext_gcbezrg(Afptext_gcbezrg afptext_gcbezrg) {
        this.afptext_gcbezrgs.add(afptext_gcbezrg);
    }

}