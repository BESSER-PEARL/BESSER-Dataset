





import java.util.List;
import java.util.ArrayList;

public class expansionmodel_Representation extends AbstractRepresentation {

    private String graphicalElementType;





    private List<expansionmodel_Representation> expansionmodel_representations;




    private List<expansionmodel_InducedRepresentation> expansionmodel_inducedrepresentations;




    private expansionmodel_InducedRepresentation expansionmodel_inducedrepresentation;


    public expansionmodel_Representation(
        String graphicalElementType    ) {
        super(
        );
        this.graphicalElementType = graphicalElementType;
        this.expansionmodel_representations = new ArrayList<>();
        this.expansionmodel_inducedrepresentations = new ArrayList<>();
    }

    public expansionmodel_Representation(
        String graphicalElementType        ArrayList<expansionmodel_Representation> expansionmodel_representations,        ArrayList<expansionmodel_InducedRepresentation> expansionmodel_inducedrepresentations    ) {
        this.graphicalElementType = graphicalElementType;
        this.expansionmodel_representations = expansionmodel_representations;
        this.expansionmodel_inducedrepresentations = expansionmodel_inducedrepresentations;
    }

    public String getGraphicalelementtype() {
        return graphicalElementType;
    }

    public void setGraphicalelementtype(String graphicalElementType) {
        this.graphicalElementType = graphicalElementType;
    }

    public List<expansionmodel_Representation> getExpansionmodel_representations() {
        return expansionmodel_representations;
    }

    public void addExpansionmodel_representation(Expansionmodel_representation expansionmodel_representation) {
        this.expansionmodel_representations.add(expansionmodel_representation);
    }
    public List<expansionmodel_InducedRepresentation> getExpansionmodel_inducedrepresentations() {
        return expansionmodel_inducedrepresentations;
    }

    public void addExpansionmodel_inducedrepresentation(Expansionmodel_inducedrepresentation expansionmodel_inducedrepresentation) {
        this.expansionmodel_inducedrepresentations.add(expansionmodel_inducedrepresentation);
    }
    public expansionmodel_InducedRepresentation getExpansionmodel_inducedrepresentation() {
        return expansionmodel_inducedrepresentation;
    }

    public void setExpansionmodel_inducedrepresentation(expansionmodel_InducedRepresentation expansionmodel_inducedrepresentation) {
        this.expansionmodel_inducedrepresentation = expansionmodel_inducedrepresentation;
    }

}