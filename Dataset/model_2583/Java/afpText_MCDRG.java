





import java.util.List;
import java.util.ArrayList;

public class afpText_MCDRG  {

    private String RGLength;





    private List<afpText_triplet> afptext_triplets;




    private afpText_MCD afptext_mcd;


    public afpText_MCDRG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MCDRG(
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
    public afpText_MCD getAfptext_mcd() {
        return afptext_mcd;
    }

    public void setAfptext_mcd(afpText_MCD afptext_mcd) {
        this.afptext_mcd = afptext_mcd;
    }

}