





import java.util.List;
import java.util.ArrayList;

public class persistence_Entity extends EntityOrView {






    private persistence_EncapsulatedAssociation persistence_encapsulatedassociation;




    private List<persistence_EntityAssociation> persistence_entityassociations;




    private persistence_EntityFeature persistence_entityfeature;




    private persistence_EncapsulatedAssociation persistence_encapsulatedassociation;




    private persistence_EntityAssociation persistence_entityassociation;




    private List<persistence_EntityFeature> persistence_entityfeatures;


    public persistence_Entity(
    ) {
        super(
        );
        this.persistence_entityassociations = new ArrayList<>();
        this.persistence_entityfeatures = new ArrayList<>();
    }

    public persistence_Entity(
        ArrayList<persistence_EntityAssociation> persistence_entityassociations,        ArrayList<persistence_EntityFeature> persistence_entityfeatures    ) {
        this.persistence_entityassociations = persistence_entityassociations;
        this.persistence_entityfeatures = persistence_entityfeatures;
    }


    public persistence_EncapsulatedAssociation getPersistence_encapsulatedassociation() {
        return persistence_encapsulatedassociation;
    }

    public void setPersistence_encapsulatedassociation(persistence_EncapsulatedAssociation persistence_encapsulatedassociation) {
        this.persistence_encapsulatedassociation = persistence_encapsulatedassociation;
    }
    public List<persistence_EntityAssociation> getPersistence_entityassociations() {
        return persistence_entityassociations;
    }

    public void addPersistence_entityassociation(Persistence_entityassociation persistence_entityassociation) {
        this.persistence_entityassociations.add(persistence_entityassociation);
    }
    public persistence_EntityFeature getPersistence_entityfeature() {
        return persistence_entityfeature;
    }

    public void setPersistence_entityfeature(persistence_EntityFeature persistence_entityfeature) {
        this.persistence_entityfeature = persistence_entityfeature;
    }
    public persistence_EncapsulatedAssociation getPersistence_encapsulatedassociation() {
        return persistence_encapsulatedassociation;
    }

    public void setPersistence_encapsulatedassociation(persistence_EncapsulatedAssociation persistence_encapsulatedassociation) {
        this.persistence_encapsulatedassociation = persistence_encapsulatedassociation;
    }
    public persistence_EntityAssociation getPersistence_entityassociation() {
        return persistence_entityassociation;
    }

    public void setPersistence_entityassociation(persistence_EntityAssociation persistence_entityassociation) {
        this.persistence_entityassociation = persistence_entityassociation;
    }
    public List<persistence_EntityFeature> getPersistence_entityfeatures() {
        return persistence_entityfeatures;
    }

    public void addPersistence_entityfeature(Persistence_entityfeature persistence_entityfeature) {
        this.persistence_entityfeatures.add(persistence_entityfeature);
    }

}