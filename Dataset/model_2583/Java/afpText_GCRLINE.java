





import java.util.List;
import java.util.ArrayList;

public class afpText_GCRLINE extends triplet {






    private List<afpText_GCRLINERG> afptext_gcrlinergs;


    public afpText_GCRLINE(
    ) {
        super(
        );
        this.afptext_gcrlinergs = new ArrayList<>();
    }

    public afpText_GCRLINE(
        ArrayList<afpText_GCRLINERG> afptext_gcrlinergs    ) {
        this.afptext_gcrlinergs = afptext_gcrlinergs;
    }


    public List<afpText_GCRLINERG> getAfptext_gcrlinergs() {
        return afptext_gcrlinergs;
    }

    public void addAfptext_gcrlinerg(Afptext_gcrlinerg afptext_gcrlinerg) {
        this.afptext_gcrlinergs.add(afptext_gcrlinerg);
    }

}