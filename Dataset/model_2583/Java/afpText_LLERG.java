





import java.util.List;
import java.util.ArrayList;

public class afpText_LLERG  {

    private String RGFunct;
    private String RGLength;





    private List<afpText_triplet> afptext_triplets;




    private afpText_LLE afptext_lle;


    public afpText_LLERG(
        String RGFunct,        String RGLength    ) {
        this.RGFunct = RGFunct;
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_LLERG(
        String RGFunct,        String RGLength        ArrayList<afpText_triplet> afptext_triplets    ) {
        this.RGFunct = RGFunct;
        this.RGLength = RGLength;
        this.afptext_triplets = afptext_triplets;
    }

    public String getRgfunct() {
        return RGFunct;
    }

    public void setRgfunct(String RGFunct) {
        this.RGFunct = RGFunct;
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
    public afpText_LLE getAfptext_lle() {
        return afptext_lle;
    }

    public void setAfptext_lle(afpText_LLE afptext_lle) {
        this.afptext_lle = afptext_lle;
    }

}