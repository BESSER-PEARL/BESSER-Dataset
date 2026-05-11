





import java.util.List;
import java.util.ArrayList;

public class afpText_GCFLT extends triplet {






    private List<afpText_GCFLTRG> afptext_gcfltrgs;


    public afpText_GCFLT(
    ) {
        super(
        );
        this.afptext_gcfltrgs = new ArrayList<>();
    }

    public afpText_GCFLT(
        ArrayList<afpText_GCFLTRG> afptext_gcfltrgs    ) {
        this.afptext_gcfltrgs = afptext_gcfltrgs;
    }


    public List<afpText_GCFLTRG> getAfptext_gcfltrgs() {
        return afptext_gcfltrgs;
    }

    public void addAfptext_gcfltrg(Afptext_gcfltrg afptext_gcfltrg) {
        this.afptext_gcfltrgs.add(afptext_gcfltrg);
    }

}