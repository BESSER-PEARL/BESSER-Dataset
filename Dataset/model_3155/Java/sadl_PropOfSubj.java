





import java.util.List;
import java.util.ArrayList;

public class sadl_PropOfSubj extends GraphPattern {






    private sadl_ResourceByName sadl_resourcebyname;




    private List<sadl_OfPhrase> sadl_ofphrases;


    public sadl_PropOfSubj(
    ) {
        super(
        );
        this.sadl_ofphrases = new ArrayList<>();
    }

    public sadl_PropOfSubj(
        ArrayList<sadl_OfPhrase> sadl_ofphrases    ) {
        this.sadl_ofphrases = sadl_ofphrases;
    }


    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }
    public List<sadl_OfPhrase> getSadl_ofphrases() {
        return sadl_ofphrases;
    }

    public void addSadl_ofphrase(Sadl_ofphrase sadl_ofphrase) {
        this.sadl_ofphrases.add(sadl_ofphrase);
    }

}