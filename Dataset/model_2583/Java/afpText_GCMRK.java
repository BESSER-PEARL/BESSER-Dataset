





import java.util.List;
import java.util.ArrayList;

public class afpText_GCMRK extends triplet {






    private List<afpText_GCMRKRG> afptext_gcmrkrgs;


    public afpText_GCMRK(
    ) {
        super(
        );
        this.afptext_gcmrkrgs = new ArrayList<>();
    }

    public afpText_GCMRK(
        ArrayList<afpText_GCMRKRG> afptext_gcmrkrgs    ) {
        this.afptext_gcmrkrgs = afptext_gcmrkrgs;
    }


    public List<afpText_GCMRKRG> getAfptext_gcmrkrgs() {
        return afptext_gcmrkrgs;
    }

    public void addAfptext_gcmrkrg(Afptext_gcmrkrg afptext_gcmrkrg) {
        this.afptext_gcmrkrgs.add(afptext_gcmrkrg);
    }

}