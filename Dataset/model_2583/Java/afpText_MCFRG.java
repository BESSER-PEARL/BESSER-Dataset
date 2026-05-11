





import java.util.List;
import java.util.ArrayList;

public class afpText_MCFRG  {

    private String RGLength;





    private afpText_MCF afptext_mcf;




    private List<afpText_triplet> afptext_triplets;


    public afpText_MCFRG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MCFRG(
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

    public afpText_MCF getAfptext_mcf() {
        return afptext_mcf;
    }

    public void setAfptext_mcf(afpText_MCF afptext_mcf) {
        this.afptext_mcf = afptext_mcf;
    }
    public List<afpText_triplet> getAfptext_triplets() {
        return afptext_triplets;
    }

    public void addAfptext_triplet(Afptext_triplet afptext_triplet) {
        this.afptext_triplets.add(afptext_triplet);
    }

}