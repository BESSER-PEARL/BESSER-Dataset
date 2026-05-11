





import java.util.List;
import java.util.ArrayList;

public class afpText_MGORG  {

    private String RGLength;





    private afpText_MGO afptext_mgo;




    private List<afpText_triplet> afptext_triplets;


    public afpText_MGORG(
        String RGLength    ) {
        this.RGLength = RGLength;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_MGORG(
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

    public afpText_MGO getAfptext_mgo() {
        return afptext_mgo;
    }

    public void setAfptext_mgo(afpText_MGO afptext_mgo) {
        this.afptext_mgo = afptext_mgo;
    }
    public List<afpText_triplet> getAfptext_triplets() {
        return afptext_triplets;
    }

    public void addAfptext_triplet(Afptext_triplet afptext_triplet) {
        this.afptext_triplets.add(afptext_triplet);
    }

}