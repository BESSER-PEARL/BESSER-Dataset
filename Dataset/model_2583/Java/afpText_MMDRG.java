





import java.util.List;
import java.util.ArrayList;

public class afpText_MMDRG  {

    private String RGLength;





    private afpText_MMD afptext_mmd;




    private List<afpText_triplet> afptext_triplets;


    public afpText_MMDRG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MMDRG(
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

    public afpText_MMD getAfptext_mmd() {
        return afptext_mmd;
    }

    public void setAfptext_mmd(afpText_MMD afptext_mmd) {
        this.afptext_mmd = afptext_mmd;
    }
    public List<afpText_triplet> getAfptext_triplets() {
        return afptext_triplets;
    }

    public void addAfptext_triplet(Afptext_triplet afptext_triplet) {
        this.afptext_triplets.add(afptext_triplet);
    }

}