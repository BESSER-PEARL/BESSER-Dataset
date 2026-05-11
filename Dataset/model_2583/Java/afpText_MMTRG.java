





import java.util.List;
import java.util.ArrayList;

public class afpText_MMTRG  {

    private String RGLength;





    private List<afpText_triplet> afptext_triplets;




    private afpText_MMT afptext_mmt;


    public afpText_MMTRG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MMTRG(
        String RGLength        ArrayList<afpText_triplet> afptext_triplets    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = afptext_triplets;
    }

    public String getRglength() {
        return RGLength;
    }

    public void setRglength(String RGLength) {
        this.RGLength = RGLength;
    }

    public List<afpText_triplet> getAfptext_triplets() {
        return afptext_triplets;
    }

    public void addAfptext_triplet(Afptext_triplet afptext_triplet) {
        this.afptext_triplets.add(afptext_triplet);
    }
    public afpText_MMT getAfptext_mmt() {
        return afptext_mmt;
    }

    public void setAfptext_mmt(afpText_MMT afptext_mmt) {
        this.afptext_mmt = afptext_mmt;
    }

}