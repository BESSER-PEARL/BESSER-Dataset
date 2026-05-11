





import java.util.List;
import java.util.ArrayList;

public class ISO20022_BusinessElement extends Member, BusinessConcept {

    private boolean isDerived;





    private ISO20022_BusinessComponent iso20022_businesscomponent;




    private ISO20022_BusinessComponent iso20022_businesscomponent;


    public ISO20022_BusinessElement(
        boolean isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
    }


    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }

    public ISO20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(ISO20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public ISO20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(ISO20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}