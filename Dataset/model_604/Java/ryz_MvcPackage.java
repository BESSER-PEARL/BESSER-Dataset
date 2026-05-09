





import java.util.List;
import java.util.ArrayList;

public class ryz_MvcPackage extends Package {






    private List<ryz_MainComponent> ryz_maincomponents;




    private List<ryz_MainComponentRelation> ryz_maincomponentrelations;


    public ryz_MvcPackage(
    ) {
        super(
        );
        this.ryz_maincomponents = new ArrayList<>();
        this.ryz_maincomponentrelations = new ArrayList<>();
    }

    public ryz_MvcPackage(
        ArrayList<ryz_MainComponent> ryz_maincomponents,        ArrayList<ryz_MainComponentRelation> ryz_maincomponentrelations    ) {
        this.ryz_maincomponents = ryz_maincomponents;
        this.ryz_maincomponentrelations = ryz_maincomponentrelations;
    }


    public List<ryz_MainComponent> getRyz_maincomponents() {
        return ryz_maincomponents;
    }

    public void addRyz_maincomponent(Ryz_maincomponent ryz_maincomponent) {
        this.ryz_maincomponents.add(ryz_maincomponent);
    }
    public List<ryz_MainComponentRelation> getRyz_maincomponentrelations() {
        return ryz_maincomponentrelations;
    }

    public void addRyz_maincomponentrelation(Ryz_maincomponentrelation ryz_maincomponentrelation) {
        this.ryz_maincomponentrelations.add(ryz_maincomponentrelation);
    }

}