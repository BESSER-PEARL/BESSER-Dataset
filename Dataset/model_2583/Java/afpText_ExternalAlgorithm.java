





import java.util.List;
import java.util.ArrayList;

public class afpText_ExternalAlgorithm extends triplet {

    private String ALGTYPE;





    private List<afpText_ExternalAlgorithmRG> afptext_externalalgorithmrgs;


    public afpText_ExternalAlgorithm(
        String ALGTYPE    ) {
        super(
        );
        this.ALGTYPE = ALGTYPE;
        this.afptext_externalalgorithmrgs = new ArrayList<>();
    }

    public afpText_ExternalAlgorithm(
        String ALGTYPE        ArrayList<afpText_ExternalAlgorithmRG> afptext_externalalgorithmrgs    ) {
        this.ALGTYPE = ALGTYPE;
        this.afptext_externalalgorithmrgs = afptext_externalalgorithmrgs;
    }

    public String getAlgtype() {
        return ALGTYPE;
    }

    public void setAlgtype(String ALGTYPE) {
        this.ALGTYPE = ALGTYPE;
    }

    public List<afpText_ExternalAlgorithmRG> getAfptext_externalalgorithmrgs() {
        return afptext_externalalgorithmrgs;
    }

    public void addAfptext_externalalgorithmrg(Afptext_externalalgorithmrg afptext_externalalgorithmrg) {
        this.afptext_externalalgorithmrgs.add(afptext_externalalgorithmrg);
    }

}