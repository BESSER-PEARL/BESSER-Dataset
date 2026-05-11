





import java.util.List;
import java.util.ArrayList;

public class carnot_DataTypeType extends IMetaType {

    private String instanceClass;
    private String evaluator;
    private String readable;
    private String panelClass;
    private String validatorClass;
    private String storageStrategy;
    private String writable;
    private String accessPathEditor;
    private String valueCreator;





    private carnot_DataType carnot_datatype;




    private carnot_AccessPointType carnot_accesspointtype;




    private List<carnot_DataType> carnot_datatypes;




    private carnot_ModelType carnot_modeltype;


    public carnot_DataTypeType(
        String instanceClass,        String evaluator,        String readable,        String panelClass,        String validatorClass,        String storageStrategy,        String writable,        String accessPathEditor,        String valueCreator    ) {
        super(
        );
        this.instanceClass = instanceClass;
        this.evaluator = evaluator;
        this.readable = readable;
        this.panelClass = panelClass;
        this.validatorClass = validatorClass;
        this.storageStrategy = storageStrategy;
        this.writable = writable;
        this.accessPathEditor = accessPathEditor;
        this.valueCreator = valueCreator;
        this.carnot_datatypes = new ArrayList<>();
    }

    public carnot_DataTypeType(
        String instanceClass,        String evaluator,        String readable,        String panelClass,        String validatorClass,        String storageStrategy,        String writable,        String accessPathEditor,        String valueCreator        ArrayList<carnot_DataType> carnot_datatypes    ) {
        this.instanceClass = instanceClass;
        this.evaluator = evaluator;
        this.readable = readable;
        this.panelClass = panelClass;
        this.validatorClass = validatorClass;
        this.storageStrategy = storageStrategy;
        this.writable = writable;
        this.accessPathEditor = accessPathEditor;
        this.valueCreator = valueCreator;
        this.carnot_datatypes = carnot_datatypes;
    }

    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }
    public String getEvaluator() {
        return evaluator;
    }

    public void setEvaluator(String evaluator) {
        this.evaluator = evaluator;
    }
    public String getReadable() {
        return readable;
    }

    public void setReadable(String readable) {
        this.readable = readable;
    }
    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getValidatorclass() {
        return validatorClass;
    }

    public void setValidatorclass(String validatorClass) {
        this.validatorClass = validatorClass;
    }
    public String getStoragestrategy() {
        return storageStrategy;
    }

    public void setStoragestrategy(String storageStrategy) {
        this.storageStrategy = storageStrategy;
    }
    public String getWritable() {
        return writable;
    }

    public void setWritable(String writable) {
        this.writable = writable;
    }
    public String getAccesspatheditor() {
        return accessPathEditor;
    }

    public void setAccesspatheditor(String accessPathEditor) {
        this.accessPathEditor = accessPathEditor;
    }
    public String getValuecreator() {
        return valueCreator;
    }

    public void setValuecreator(String valueCreator) {
        this.valueCreator = valueCreator;
    }

    public carnot_DataType getCarnot_datatype() {
        return carnot_datatype;
    }

    public void setCarnot_datatype(carnot_DataType carnot_datatype) {
        this.carnot_datatype = carnot_datatype;
    }
    public carnot_AccessPointType getCarnot_accesspointtype() {
        return carnot_accesspointtype;
    }

    public void setCarnot_accesspointtype(carnot_AccessPointType carnot_accesspointtype) {
        this.carnot_accesspointtype = carnot_accesspointtype;
    }
    public List<carnot_DataType> getCarnot_datatypes() {
        return carnot_datatypes;
    }

    public void addCarnot_datatype(Carnot_datatype carnot_datatype) {
        this.carnot_datatypes.add(carnot_datatype);
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}