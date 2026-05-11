





import java.util.List;
import java.util.ArrayList;

public class afpText_MPGRG  {

    private String RGLength;





    private List<afpText_triplet> afptext_triplets;




    private afpText_MPG afptext_mpg;


    public afpText_MPGRG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MPGRG(
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
    public afpText_MPG getAfptext_mpg() {
        return afptext_mpg;
    }

    public void setAfptext_mpg(afpText_MPG afptext_mpg) {
        this.afptext_mpg = afptext_mpg;
    }

}