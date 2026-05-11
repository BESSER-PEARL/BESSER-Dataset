





import java.util.List;
import java.util.ArrayList;

public class persistence_ViewAssociation extends Association, NamedDisplayElement, ViewFeature {

    private String cardinality;





    private persistence_EncapsulatedAssociation persistence_encapsulatedassociation;


    public persistence_ViewAssociation(
        String cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }

    public persistence_EncapsulatedAssociation getPersistence_encapsulatedassociation() {
        return persistence_encapsulatedassociation;
    }

    public void setPersistence_encapsulatedassociation(persistence_EncapsulatedAssociation persistence_encapsulatedassociation) {
        this.persistence_encapsulatedassociation = persistence_encapsulatedassociation;
    }

}