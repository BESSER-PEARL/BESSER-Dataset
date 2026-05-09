





import java.util.List;
import java.util.ArrayList;

public class rapidml_ReferenceProperty extends Feature, ReferenceElement {

    private boolean containment;
    private boolean container;





    private rapidml_ReferenceProperty rapidml_referenceproperty;


    public rapidml_ReferenceProperty(
        boolean containment,        boolean container    ) {
        super(
        );
        this.containment = containment;
        this.container = container;
    }


    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }
    public boolean getContainer() {
        return container;
    }

    public void setContainer(boolean container) {
        this.container = container;
    }

    public rapidml_ReferenceProperty getRapidml_referenceproperty() {
        return rapidml_referenceproperty;
    }

    public void setRapidml_referenceproperty(rapidml_ReferenceProperty rapidml_referenceproperty) {
        this.rapidml_referenceproperty = rapidml_referenceproperty;
    }

}