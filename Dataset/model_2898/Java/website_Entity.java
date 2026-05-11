





import java.util.List;
import java.util.ArrayList;

public class website_Entity extends EntityOrView {






    private List<website_EntityAssociation> website_entityassociations;




    private website_EncapsulatedAssociation website_encapsulatedassociation;




    private website_EntityFeature website_entityfeature;




    private List<website_EntityFeature> website_entityfeatures;




    private website_EncapsulatedAssociation website_encapsulatedassociation;




    private website_EntityAssociation website_entityassociation;


    public website_Entity(
    ) {
        super(
        );
        this.website_entityassociations = new ArrayList<>();
        this.website_entityfeatures = new ArrayList<>();
    }

    public website_Entity(
        ArrayList<website_EntityAssociation> website_entityassociations,        ArrayList<website_EntityFeature> website_entityfeatures    ) {
        this.website_entityassociations = website_entityassociations;
        this.website_entityfeatures = website_entityfeatures;
    }


    public List<website_EntityAssociation> getWebsite_entityassociations() {
        return website_entityassociations;
    }

    public void addWebsite_entityassociation(Website_entityassociation website_entityassociation) {
        this.website_entityassociations.add(website_entityassociation);
    }
    public website_EncapsulatedAssociation getWebsite_encapsulatedassociation() {
        return website_encapsulatedassociation;
    }

    public void setWebsite_encapsulatedassociation(website_EncapsulatedAssociation website_encapsulatedassociation) {
        this.website_encapsulatedassociation = website_encapsulatedassociation;
    }
    public website_EntityFeature getWebsite_entityfeature() {
        return website_entityfeature;
    }

    public void setWebsite_entityfeature(website_EntityFeature website_entityfeature) {
        this.website_entityfeature = website_entityfeature;
    }
    public List<website_EntityFeature> getWebsite_entityfeatures() {
        return website_entityfeatures;
    }

    public void addWebsite_entityfeature(Website_entityfeature website_entityfeature) {
        this.website_entityfeatures.add(website_entityfeature);
    }
    public website_EncapsulatedAssociation getWebsite_encapsulatedassociation() {
        return website_encapsulatedassociation;
    }

    public void setWebsite_encapsulatedassociation(website_EncapsulatedAssociation website_encapsulatedassociation) {
        this.website_encapsulatedassociation = website_encapsulatedassociation;
    }
    public website_EntityAssociation getWebsite_entityassociation() {
        return website_entityassociation;
    }

    public void setWebsite_entityassociation(website_EntityAssociation website_entityassociation) {
        this.website_entityassociation = website_entityassociation;
    }

}