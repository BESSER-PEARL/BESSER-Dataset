





import java.util.List;
import java.util.ArrayList;

public class expansionmodel_GraphicalElementLibrary  {

    private String name;





    private List<expansionmodel_AbstractRepresentation> expansionmodel_abstractrepresentations;




    private List<expansionmodel_RepresentationKind> expansionmodel_representationkinds;


    public expansionmodel_GraphicalElementLibrary(
        String name    ) {
        this.name = name;
        this.expansionmodel_abstractrepresentations = new ArrayList<>();
        this.expansionmodel_representationkinds = new ArrayList<>();
    }

    public expansionmodel_GraphicalElementLibrary(
        String name        ArrayList<expansionmodel_AbstractRepresentation> expansionmodel_abstractrepresentations,        ArrayList<expansionmodel_RepresentationKind> expansionmodel_representationkinds    ) {
        this.name = name;
        this.expansionmodel_abstractrepresentations = expansionmodel_abstractrepresentations;
        this.expansionmodel_representationkinds = expansionmodel_representationkinds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<expansionmodel_AbstractRepresentation> getExpansionmodel_abstractrepresentations() {
        return expansionmodel_abstractrepresentations;
    }

    public void addExpansionmodel_abstractrepresentation(Expansionmodel_abstractrepresentation expansionmodel_abstractrepresentation) {
        this.expansionmodel_abstractrepresentations.add(expansionmodel_abstractrepresentation);
    }
    public List<expansionmodel_RepresentationKind> getExpansionmodel_representationkinds() {
        return expansionmodel_representationkinds;
    }

    public void addExpansionmodel_representationkind(Expansionmodel_representationkind expansionmodel_representationkind) {
        this.expansionmodel_representationkinds.add(expansionmodel_representationkind);
    }

}