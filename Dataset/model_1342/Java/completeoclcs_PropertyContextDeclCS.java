





import java.util.List;
import java.util.ArrayList;

public class completeoclcs_PropertyContextDeclCS extends FeatureContextDeclCS {






    private List<completeoclcs_ConstraintCS> completeoclcs_constraintcss;




    private List<completeoclcs_ExpSpecificationCS> completeoclcs_expspecificationcss;


    public completeoclcs_PropertyContextDeclCS(
    ) {
        super(
        );
        this.completeoclcs_constraintcss = new ArrayList<>();
        this.completeoclcs_expspecificationcss = new ArrayList<>();
    }

    public completeoclcs_PropertyContextDeclCS(
        ArrayList<completeoclcs_ConstraintCS> completeoclcs_constraintcss,        ArrayList<completeoclcs_ExpSpecificationCS> completeoclcs_expspecificationcss    ) {
        this.completeoclcs_constraintcss = completeoclcs_constraintcss;
        this.completeoclcs_expspecificationcss = completeoclcs_expspecificationcss;
    }


    public List<completeoclcs_ConstraintCS> getCompleteoclcs_constraintcss() {
        return completeoclcs_constraintcss;
    }

    public void addCompleteoclcs_constraintcs(Completeoclcs_constraintcs completeoclcs_constraintcs) {
        this.completeoclcs_constraintcss.add(completeoclcs_constraintcs);
    }
    public List<completeoclcs_ExpSpecificationCS> getCompleteoclcs_expspecificationcss() {
        return completeoclcs_expspecificationcss;
    }

    public void addCompleteoclcs_expspecificationcs(Completeoclcs_expspecificationcs completeoclcs_expspecificationcs) {
        this.completeoclcs_expspecificationcss.add(completeoclcs_expspecificationcs);
    }

}