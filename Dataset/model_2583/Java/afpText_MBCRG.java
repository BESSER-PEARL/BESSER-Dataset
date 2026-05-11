





import java.util.List;
import java.util.ArrayList;

public class afpText_MBCRG  {

    private String RGLength;





    private List<afpText_triplet> afptext_triplets;




    private afpText_MBC afptext_mbc;


    public afpText_MBCRG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MBCRG(
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
    public afpText_MBC getAfptext_mbc() {
        return afptext_mbc;
    }

    public void setAfptext_mbc(afpText_MBC afptext_mbc) {
        this.afptext_mbc = afptext_mbc;
    }

}