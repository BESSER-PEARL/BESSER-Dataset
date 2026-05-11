





import java.util.List;
import java.util.ArrayList;

public class afpText_MIORG  {

    private String RGLength;





    private afpText_MIO afptext_mio;




    private List<afpText_triplet> afptext_triplets;


    public afpText_MIORG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MIORG(
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

    public afpText_MIO getAfptext_mio() {
        return afptext_mio;
    }

    public void setAfptext_mio(afpText_MIO afptext_mio) {
        this.afptext_mio = afptext_mio;
    }
    public List<afpText_triplet> getAfptext_triplets() {
        return afptext_triplets;
    }

    public void addAfptext_triplet(Afptext_triplet afptext_triplet) {
        this.afptext_triplets.add(afptext_triplet);
    }

}