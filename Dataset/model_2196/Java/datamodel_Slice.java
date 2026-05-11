





import java.util.List;
import java.util.ArrayList;

public class datamodel_Slice  {

    private String name;
    private String diagram;





    private List<datamodel_Constraint> datamodel_constraints;




    private List<datamodel_Ensemble> datamodel_ensembles;




    private datamodel_Ensemble datamodel_ensemble;


    public datamodel_Slice(
        String name,        String diagram    ) {
        this.name = name;
        this.diagram = diagram;
        this.datamodel_constraints = new ArrayList<>();
        this.datamodel_ensembles = new ArrayList<>();
    }

    public datamodel_Slice(
        String name,        String diagram        ArrayList<datamodel_Constraint> datamodel_constraints,        ArrayList<datamodel_Ensemble> datamodel_ensembles    ) {
        this.name = name;
        this.diagram = diagram;
        this.datamodel_constraints = datamodel_constraints;
        this.datamodel_ensembles = datamodel_ensembles;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDiagram() {
        return diagram;
    }

    public void setDiagram(String diagram) {
        this.diagram = diagram;
    }

    public List<datamodel_Constraint> getDatamodel_constraints() {
        return datamodel_constraints;
    }

    public void addDatamodel_constraint(Datamodel_constraint datamodel_constraint) {
        this.datamodel_constraints.add(datamodel_constraint);
    }
    public List<datamodel_Ensemble> getDatamodel_ensembles() {
        return datamodel_ensembles;
    }

    public void addDatamodel_ensemble(Datamodel_ensemble datamodel_ensemble) {
        this.datamodel_ensembles.add(datamodel_ensemble);
    }
    public datamodel_Ensemble getDatamodel_ensemble() {
        return datamodel_ensemble;
    }

    public void setDatamodel_ensemble(datamodel_Ensemble datamodel_ensemble) {
        this.datamodel_ensemble = datamodel_ensemble;
    }

}