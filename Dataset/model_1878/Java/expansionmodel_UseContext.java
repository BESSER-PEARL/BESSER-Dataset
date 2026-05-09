





import java.util.List;
import java.util.ArrayList;

public class expansionmodel_UseContext  {

    private String name;
    private String diagramType;





    private List<expansionmodel_Representation> expansionmodel_representations;


    public expansionmodel_UseContext(
        String name,        String diagramType    ) {
        this.name = name;
        this.diagramType = diagramType;
        this.expansionmodel_representations = new ArrayList<>();
    }

    public expansionmodel_UseContext(
        String name,        String diagramType        ArrayList<expansionmodel_Representation> expansionmodel_representations    ) {
        this.name = name;
        this.diagramType = diagramType;
        this.expansionmodel_representations = expansionmodel_representations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDiagramtype() {
        return diagramType;
    }

    public void setDiagramtype(String diagramType) {
        this.diagramType = diagramType;
    }

    public List<expansionmodel_Representation> getExpansionmodel_representations() {
        return expansionmodel_representations;
    }

    public void addExpansionmodel_representation(Expansionmodel_representation expansionmodel_representation) {
        this.expansionmodel_representations.add(expansionmodel_representation);
    }

}