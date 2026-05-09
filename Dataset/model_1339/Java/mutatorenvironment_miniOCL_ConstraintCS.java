





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_miniOCL_ConstraintCS  {






    private PathNameCS pathnamecs;




    private List<InvariantCS> invariantcss;


    public mutatorenvironment_miniOCL_ConstraintCS(
    ) {
        this.invariantcss = new ArrayList<>();
    }

    public mutatorenvironment_miniOCL_ConstraintCS(
        ArrayList<InvariantCS> invariantcss    ) {
        this.invariantcss = invariantcss;
    }


    public PathNameCS getPathnamecs() {
        return pathnamecs;
    }

    public void setPathnamecs(PathNameCS pathnamecs) {
        this.pathnamecs = pathnamecs;
    }
    public List<InvariantCS> getInvariantcss() {
        return invariantcss;
    }

    public void addInvariantcs(Invariantcs invariantcs) {
        this.invariantcss.add(invariantcs);
    }

}