





import java.util.List;
import java.util.ArrayList;

public class ryz_ModelPackage extends ComponentPackage {






    private List<ryz_ModelAssociation> ryz_modelassociations;


    public ryz_ModelPackage(
    ) {
        super(
        );
        this.ryz_modelassociations = new ArrayList<>();
    }

    public ryz_ModelPackage(
        ArrayList<ryz_ModelAssociation> ryz_modelassociations    ) {
        this.ryz_modelassociations = ryz_modelassociations;
    }


    public List<ryz_ModelAssociation> getRyz_modelassociations() {
        return ryz_modelassociations;
    }

    public void addRyz_modelassociation(Ryz_modelassociation ryz_modelassociation) {
        this.ryz_modelassociations.add(ryz_modelassociation);
    }

}