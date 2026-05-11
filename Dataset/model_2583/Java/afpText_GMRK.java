





import java.util.List;
import java.util.ArrayList;

public class afpText_GMRK extends triplet {






    private List<afpText_GMRKRG> afptext_gmrkrgs;


    public afpText_GMRK(
    ) {
        super(
        );
        this.afptext_gmrkrgs = new ArrayList<>();
    }

    public afpText_GMRK(
        ArrayList<afpText_GMRKRG> afptext_gmrkrgs    ) {
        this.afptext_gmrkrgs = afptext_gmrkrgs;
    }


    public List<afpText_GMRKRG> getAfptext_gmrkrgs() {
        return afptext_gmrkrgs;
    }

    public void addAfptext_gmrkrg(Afptext_gmrkrg afptext_gmrkrg) {
        this.afptext_gmrkrgs.add(afptext_gmrkrg);
    }

}