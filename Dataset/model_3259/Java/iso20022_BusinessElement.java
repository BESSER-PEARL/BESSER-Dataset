





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessElement extends BusinessConcept, Construct {

    private boolean isDerived;





    private iso20022_BusinessElementType iso20022_businesselementtype;




    private iso20022_BusinessComponent iso20022_businesscomponent;




    private iso20022_BusinessComponent iso20022_businesscomponent;


    public iso20022_BusinessElement(
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

    public iso20022_BusinessElementType getIso20022_businesselementtype() {
        return iso20022_businesselementtype;
    }

    public void setIso20022_businesselementtype(iso20022_BusinessElementType iso20022_businesselementtype) {
        this.iso20022_businesselementtype = iso20022_businesselementtype;
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}