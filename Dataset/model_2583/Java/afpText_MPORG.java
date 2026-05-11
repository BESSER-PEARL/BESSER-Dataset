





import java.util.List;
import java.util.ArrayList;

public class afpText_MPORG  {

    private String RGLength;





    private List<afpText_triplet> afptext_triplets;




    private afpText_MPO afptext_mpo;


    public afpText_MPORG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MPORG(
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
    public afpText_MPO getAfptext_mpo() {
        return afptext_mpo;
    }

    public void setAfptext_mpo(afpText_MPO afptext_mpo) {
        this.afptext_mpo = afptext_mpo;
    }

}