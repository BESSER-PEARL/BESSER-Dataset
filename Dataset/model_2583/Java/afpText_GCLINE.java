





import java.util.List;
import java.util.ArrayList;

public class afpText_GCLINE extends triplet {






    private List<afpText_GCLINERG> afptext_gclinergs;


    public afpText_GCLINE(
    ) {
        super(
        );
        this.afptext_gclinergs = new ArrayList<>();
    }

    public afpText_GCLINE(
        ArrayList<afpText_GCLINERG> afptext_gclinergs    ) {
        this.afptext_gclinergs = afptext_gclinergs;
    }


    public List<afpText_GCLINERG> getAfptext_gclinergs() {
        return afptext_gclinergs;
    }

    public void addAfptext_gclinerg(Afptext_gclinerg afptext_gclinerg) {
        this.afptext_gclinergs.add(afptext_gclinerg);
    }

}