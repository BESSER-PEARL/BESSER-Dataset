





import java.util.List;
import java.util.ArrayList;

public class afpText_GFLT extends triplet {






    private List<afpText_GFLTRG> afptext_gfltrgs;


    public afpText_GFLT(
    ) {
        super(
        );
        this.afptext_gfltrgs = new ArrayList<>();
    }

    public afpText_GFLT(
        ArrayList<afpText_GFLTRG> afptext_gfltrgs    ) {
        this.afptext_gfltrgs = afptext_gfltrgs;
    }


    public List<afpText_GFLTRG> getAfptext_gfltrgs() {
        return afptext_gfltrgs;
    }

    public void addAfptext_gfltrg(Afptext_gfltrg afptext_gfltrg) {
        this.afptext_gfltrgs.add(afptext_gfltrg);
    }

}