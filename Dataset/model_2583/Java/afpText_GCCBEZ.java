





import java.util.List;
import java.util.ArrayList;

public class afpText_GCCBEZ extends triplet {






    private List<afpText_GCCBEZRG> afptext_gccbezrgs;


    public afpText_GCCBEZ(
    ) {
        super(
        );
        this.afptext_gccbezrgs = new ArrayList<>();
    }

    public afpText_GCCBEZ(
        ArrayList<afpText_GCCBEZRG> afptext_gccbezrgs    ) {
        this.afptext_gccbezrgs = afptext_gccbezrgs;
    }


    public List<afpText_GCCBEZRG> getAfptext_gccbezrgs() {
        return afptext_gccbezrgs;
    }

    public void addAfptext_gccbezrg(Afptext_gccbezrg afptext_gccbezrg) {
        this.afptext_gccbezrgs.add(afptext_gccbezrg);
    }

}