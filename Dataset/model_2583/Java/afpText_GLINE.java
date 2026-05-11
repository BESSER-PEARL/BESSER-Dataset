





import java.util.List;
import java.util.ArrayList;

public class afpText_GLINE extends triplet {






    private List<afpText_GLINERG> afptext_glinergs;


    public afpText_GLINE(
    ) {
        super(
        );
        this.afptext_glinergs = new ArrayList<>();
    }

    public afpText_GLINE(
        ArrayList<afpText_GLINERG> afptext_glinergs    ) {
        this.afptext_glinergs = afptext_glinergs;
    }


    public List<afpText_GLINERG> getAfptext_glinergs() {
        return afptext_glinergs;
    }

    public void addAfptext_glinerg(Afptext_glinerg afptext_glinerg) {
        this.afptext_glinergs.add(afptext_glinerg);
    }

}