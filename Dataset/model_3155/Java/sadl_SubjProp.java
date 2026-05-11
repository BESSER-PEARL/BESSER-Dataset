





import java.util.List;
import java.util.ArrayList;

public class sadl_SubjProp extends GraphPattern {






    private sadl_ResourceByName sadl_resourcebyname;




    private List<sadl_WithPhrase> sadl_withphrases;


    public sadl_SubjProp(
    ) {
        super(
        );
        this.sadl_withphrases = new ArrayList<>();
    }

    public sadl_SubjProp(
        ArrayList<sadl_WithPhrase> sadl_withphrases    ) {
        this.sadl_withphrases = sadl_withphrases;
    }


    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }
    public List<sadl_WithPhrase> getSadl_withphrases() {
        return sadl_withphrases;
    }

    public void addSadl_withphrase(Sadl_withphrase sadl_withphrase) {
        this.sadl_withphrases.add(sadl_withphrase);
    }

}