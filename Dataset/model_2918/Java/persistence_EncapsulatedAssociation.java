





import java.util.List;
import java.util.ArrayList;

public class persistence_EncapsulatedAssociation extends Association, EncapsulatedFeature {

    private String name;
    private String cardinality;
    private boolean isSourceAssociation;





    private persistence_EncapsulatedAssociation persistence_encapsulatedassociation;




    private persistence_Association persistence_association;




    private persistence_Association persistence_association;


    public persistence_EncapsulatedAssociation(
        String name,        String cardinality,        boolean isSourceAssociation    ) {
        super(
        );
        this.name = name;
        this.cardinality = cardinality;
        this.isSourceAssociation = isSourceAssociation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public boolean getIssourceassociation() {
        return isSourceAssociation;
    }

    public void setIssourceassociation(boolean isSourceAssociation) {
        this.isSourceAssociation = isSourceAssociation;
    }

    public persistence_EncapsulatedAssociation getPersistence_encapsulatedassociation() {
        return persistence_encapsulatedassociation;
    }

    public void setPersistence_encapsulatedassociation(persistence_EncapsulatedAssociation persistence_encapsulatedassociation) {
        this.persistence_encapsulatedassociation = persistence_encapsulatedassociation;
    }
    public persistence_Association getPersistence_association() {
        return persistence_association;
    }

    public void setPersistence_association(persistence_Association persistence_association) {
        this.persistence_association = persistence_association;
    }
    public persistence_Association getPersistence_association() {
        return persistence_association;
    }

    public void setPersistence_association(persistence_Association persistence_association) {
        this.persistence_association = persistence_association;
    }

}