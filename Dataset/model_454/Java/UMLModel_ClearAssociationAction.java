





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ClearAssociationAction extends Action {

    private String association;



    public UMLModel_ClearAssociationAction(
        String association    ) {
        super(
        );
        this.association = association;
    }


    public String getAssociation() {
        return association;
    }

    public void setAssociation(String association) {
        this.association = association;
    }


}