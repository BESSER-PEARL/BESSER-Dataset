





import java.util.List;
import java.util.ArrayList;

public class sadl_MergedTriples extends GraphPattern {






    private sadl_TypedBNode sadl_typedbnode;




    private List<sadl_OfPhrase> sadl_ofphrases;




    private List<sadl_WithChain> sadl_withchains;


    public sadl_MergedTriples(
    ) {
        super(
        );
        this.sadl_ofphrases = new ArrayList<>();
        this.sadl_withchains = new ArrayList<>();
    }

    public sadl_MergedTriples(
        ArrayList<sadl_OfPhrase> sadl_ofphrases,        ArrayList<sadl_WithChain> sadl_withchains    ) {
        this.sadl_ofphrases = sadl_ofphrases;
        this.sadl_withchains = sadl_withchains;
    }


    public sadl_TypedBNode getSadl_typedbnode() {
        return sadl_typedbnode;
    }

    public void setSadl_typedbnode(sadl_TypedBNode sadl_typedbnode) {
        this.sadl_typedbnode = sadl_typedbnode;
    }
    public List<sadl_OfPhrase> getSadl_ofphrases() {
        return sadl_ofphrases;
    }

    public void addSadl_ofphrase(Sadl_ofphrase sadl_ofphrase) {
        this.sadl_ofphrases.add(sadl_ofphrase);
    }
    public List<sadl_WithChain> getSadl_withchains() {
        return sadl_withchains;
    }

    public void addSadl_withchain(Sadl_withchain sadl_withchain) {
        this.sadl_withchains.add(sadl_withchain);
    }

}