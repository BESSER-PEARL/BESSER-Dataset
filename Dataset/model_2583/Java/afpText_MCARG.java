





import java.util.List;
import java.util.ArrayList;

public class afpText_MCARG  {

    private String RGLength;





    private afpText_MCA afptext_mca;




    private List<afpText_triplet> afptext_triplets;


    public afpText_MCARG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MCARG(
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

    public afpText_MCA getAfptext_mca() {
        return afptext_mca;
    }

    public void setAfptext_mca(afpText_MCA afptext_mca) {
        this.afptext_mca = afptext_mca;
    }
    public List<afpText_triplet> getAfptext_triplets() {
        return afptext_triplets;
    }

    public void addAfptext_triplet(Afptext_triplet afptext_triplet) {
        this.afptext_triplets.add(afptext_triplet);
    }

}