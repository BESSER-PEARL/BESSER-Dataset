





import java.util.List;
import java.util.ArrayList;

public class model_change_MergingSolution extends Solution {






    private List<change_ModelChangePackage> change_modelchangepackages;


    public model_change_MergingSolution(
    ) {
        super(
        );
        this.change_modelchangepackages = new ArrayList<>();
    }

    public model_change_MergingSolution(
        ArrayList<change_ModelChangePackage> change_modelchangepackages    ) {
        this.change_modelchangepackages = change_modelchangepackages;
    }


    public List<change_ModelChangePackage> getChange_modelchangepackages() {
        return change_modelchangepackages;
    }

    public void addChange_modelchangepackage(Change_modelchangepackage change_modelchangepackage) {
        this.change_modelchangepackages.add(change_modelchangepackage);
    }

}