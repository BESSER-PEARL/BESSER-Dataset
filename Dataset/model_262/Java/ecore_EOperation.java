





import java.util.List;
import java.util.ArrayList;

public class ecore_EOperation extends ETypedElement {






    private List<ecore_EParameter> ecore_eparameters;




    private ecore_EParameter ecore_eparameter;


    public ecore_EOperation(
    ) {
        super(
        );
        this.ecore_eparameters = new ArrayList<>();
    }

    public ecore_EOperation(
        ArrayList<ecore_EParameter> ecore_eparameters    ) {
        this.ecore_eparameters = ecore_eparameters;
    }


    public List<ecore_EParameter> getEcore_eparameters() {
        return ecore_eparameters;
    }

    public void addEcore_eparameter(Ecore_eparameter ecore_eparameter) {
        this.ecore_eparameters.add(ecore_eparameter);
    }
    public ecore_EParameter getEcore_eparameter() {
        return ecore_eparameter;
    }

    public void setEcore_eparameter(ecore_EParameter ecore_eparameter) {
        this.ecore_eparameter = ecore_eparameter;
    }

}