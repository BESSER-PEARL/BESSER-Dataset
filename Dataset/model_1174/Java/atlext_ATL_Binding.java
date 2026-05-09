





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_Binding extends LocatedElement {

    private String propertyName;
    private String isAssignment;





    private ATL_atlext_EObject atl_atlext_eobject;


    public atlext_ATL_Binding(
        String propertyName,        String isAssignment    ) {
        super(
        );
        this.propertyName = propertyName;
        this.isAssignment = isAssignment;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }
    public String getIsassignment() {
        return isAssignment;
    }

    public void setIsassignment(String isAssignment) {
        this.isAssignment = isAssignment;
    }

    public ATL_atlext_EObject getAtl_atlext_eobject() {
        return atl_atlext_eobject;
    }

    public void setAtl_atlext_eobject(ATL_atlext_EObject atl_atlext_eobject) {
        this.atl_atlext_eobject = atl_atlext_eobject;
    }

}