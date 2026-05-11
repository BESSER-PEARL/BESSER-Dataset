





import java.util.List;
import java.util.ArrayList;

public class website_Association extends Feature {

    private int serializationMaxDepth;
    private boolean pseudo;
    private String inputClass;





    private website_EntityOrView website_entityorview;




    private website_EntityOrView website_entityorview;




    private website_EntityOrView website_entityorview;




    private website_EncapsulatedAssociation website_encapsulatedassociation;




    private website_EntityOrView website_entityorview;




    private website_Selection website_selection;




    private List<website_EncapsulatedAssociation> website_encapsulatedassociations;


    public website_Association(
        int serializationMaxDepth,        boolean pseudo,        String inputClass    ) {
        super(
        );
        this.serializationMaxDepth = serializationMaxDepth;
        this.pseudo = pseudo;
        this.inputClass = inputClass;
        this.website_encapsulatedassociations = new ArrayList<>();
    }

    public website_Association(
        int serializationMaxDepth,        boolean pseudo,        String inputClass        ArrayList<website_EncapsulatedAssociation> website_encapsulatedassociations    ) {
        this.serializationMaxDepth = serializationMaxDepth;
        this.pseudo = pseudo;
        this.inputClass = inputClass;
        this.website_encapsulatedassociations = website_encapsulatedassociations;
    }

    public int getSerializationmaxdepth() {
        return serializationMaxDepth;
    }

    public void setSerializationmaxdepth(int serializationMaxDepth) {
        this.serializationMaxDepth = serializationMaxDepth;
    }
    public boolean getPseudo() {
        return pseudo;
    }

    public void setPseudo(boolean pseudo) {
        this.pseudo = pseudo;
    }
    public String getInputclass() {
        return inputClass;
    }

    public void setInputclass(String inputClass) {
        this.inputClass = inputClass;
    }

    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }
    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }
    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }
    public website_EncapsulatedAssociation getWebsite_encapsulatedassociation() {
        return website_encapsulatedassociation;
    }

    public void setWebsite_encapsulatedassociation(website_EncapsulatedAssociation website_encapsulatedassociation) {
        this.website_encapsulatedassociation = website_encapsulatedassociation;
    }
    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }
    public website_Selection getWebsite_selection() {
        return website_selection;
    }

    public void setWebsite_selection(website_Selection website_selection) {
        this.website_selection = website_selection;
    }
    public List<website_EncapsulatedAssociation> getWebsite_encapsulatedassociations() {
        return website_encapsulatedassociations;
    }

    public void addWebsite_encapsulatedassociation(Website_encapsulatedassociation website_encapsulatedassociation) {
        this.website_encapsulatedassociations.add(website_encapsulatedassociation);
    }

}