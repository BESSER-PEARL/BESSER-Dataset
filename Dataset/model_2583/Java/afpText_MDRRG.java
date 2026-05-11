





import java.util.List;
import java.util.ArrayList;

public class afpText_MDRRG  {

    private String RGLength;





    private List<afpText_triplet> afptext_triplets;




    private afpText_MDR afptext_mdr;


    public afpText_MDRRG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MDRRG(
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
    public afpText_MDR getAfptext_mdr() {
        return afptext_mdr;
    }

    public void setAfptext_mdr(afpText_MDR afptext_mdr) {
        this.afptext_mdr = afptext_mdr;
    }

}