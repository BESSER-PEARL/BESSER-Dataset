





import java.util.List;
import java.util.ArrayList;

public class builderState_ResourceDescription  {

    private String importedNames;
    private String URI;





    private List<builderState_IEObjectDescription> builderstate_ieobjectdescriptions;




    private List<builderState_IReferenceDescription> builderstate_ireferencedescriptions;


    public builderState_ResourceDescription(
        String importedNames,        String URI    ) {
        this.importedNames = importedNames;
        this.URI = URI;
        this.builderstate_ieobjectdescriptions = new ArrayList<>();
        this.builderstate_ireferencedescriptions = new ArrayList<>();
    }

    public builderState_ResourceDescription(
        String importedNames,        String URI        ArrayList<builderState_IEObjectDescription> builderstate_ieobjectdescriptions,        ArrayList<builderState_IReferenceDescription> builderstate_ireferencedescriptions    ) {
        this.importedNames = importedNames;
        this.URI = URI;
        this.builderstate_ieobjectdescriptions = builderstate_ieobjectdescriptions;
        this.builderstate_ireferencedescriptions = builderstate_ireferencedescriptions;
    }

    public String getImportednames() {
        return importedNames;
    }

    public void setImportednames(String importedNames) {
        this.importedNames = importedNames;
    }
    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public List<builderState_IEObjectDescription> getBuilderstate_ieobjectdescriptions() {
        return builderstate_ieobjectdescriptions;
    }

    public void addBuilderstate_ieobjectdescription(Builderstate_ieobjectdescription builderstate_ieobjectdescription) {
        this.builderstate_ieobjectdescriptions.add(builderstate_ieobjectdescription);
    }
    public List<builderState_IReferenceDescription> getBuilderstate_ireferencedescriptions() {
        return builderstate_ireferencedescriptions;
    }

    public void addBuilderstate_ireferencedescription(Builderstate_ireferencedescription builderstate_ireferencedescription) {
        this.builderstate_ireferencedescriptions.add(builderstate_ireferencedescription);
    }

}