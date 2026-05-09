





import java.util.List;
import java.util.ArrayList;

public class ryz_ControllerToModelRelation extends MainComponentRelation {

    private String modelOperation;
    private String modelCardinality;





    private ryz_Model ryz_model;




    private List<ryz_Property> ryz_propertys;




    private ryz_ActionMethod ryz_actionmethod;


    public ryz_ControllerToModelRelation(
        String modelOperation,        String modelCardinality    ) {
        super(
        );
        this.modelOperation = modelOperation;
        this.modelCardinality = modelCardinality;
        this.ryz_propertys = new ArrayList<>();
    }

    public ryz_ControllerToModelRelation(
        String modelOperation,        String modelCardinality        ArrayList<ryz_Property> ryz_propertys    ) {
        this.modelOperation = modelOperation;
        this.modelCardinality = modelCardinality;
        this.ryz_propertys = ryz_propertys;
    }

    public String getModeloperation() {
        return modelOperation;
    }

    public void setModeloperation(String modelOperation) {
        this.modelOperation = modelOperation;
    }
    public String getModelcardinality() {
        return modelCardinality;
    }

    public void setModelcardinality(String modelCardinality) {
        this.modelCardinality = modelCardinality;
    }

    public ryz_Model getRyz_model() {
        return ryz_model;
    }

    public void setRyz_model(ryz_Model ryz_model) {
        this.ryz_model = ryz_model;
    }
    public List<ryz_Property> getRyz_propertys() {
        return ryz_propertys;
    }

    public void addRyz_property(Ryz_property ryz_property) {
        this.ryz_propertys.add(ryz_property);
    }
    public ryz_ActionMethod getRyz_actionmethod() {
        return ryz_actionmethod;
    }

    public void setRyz_actionmethod(ryz_ActionMethod ryz_actionmethod) {
        this.ryz_actionmethod = ryz_actionmethod;
    }

}