





import java.util.List;
import java.util.ArrayList;

public class rapidml_Structure extends WithDataExamples, DataType, Inheritable {






    private rapidml_ReferenceProperty rapidml_referenceproperty;




    private rapidml_RealizationContainer rapidml_realizationcontainer;




    private List<rapidml_Operation> rapidml_operations;




    private rapidml_Structure rapidml_structure;




    private List<rapidml_Feature> rapidml_features;




    private rapidml_ReferenceElement rapidml_referenceelement;




    private rapidml_Feature rapidml_feature;


    public rapidml_Structure(
    ) {
        super(
        );
        this.rapidml_operations = new ArrayList<>();
        this.rapidml_features = new ArrayList<>();
    }

    public rapidml_Structure(
        ArrayList<rapidml_Operation> rapidml_operations,        ArrayList<rapidml_Feature> rapidml_features    ) {
        this.rapidml_operations = rapidml_operations;
        this.rapidml_features = rapidml_features;
    }


    public rapidml_ReferenceProperty getRapidml_referenceproperty() {
        return rapidml_referenceproperty;
    }

    public void setRapidml_referenceproperty(rapidml_ReferenceProperty rapidml_referenceproperty) {
        this.rapidml_referenceproperty = rapidml_referenceproperty;
    }
    public rapidml_RealizationContainer getRapidml_realizationcontainer() {
        return rapidml_realizationcontainer;
    }

    public void setRapidml_realizationcontainer(rapidml_RealizationContainer rapidml_realizationcontainer) {
        this.rapidml_realizationcontainer = rapidml_realizationcontainer;
    }
    public List<rapidml_Operation> getRapidml_operations() {
        return rapidml_operations;
    }

    public void addRapidml_operation(Rapidml_operation rapidml_operation) {
        this.rapidml_operations.add(rapidml_operation);
    }
    public rapidml_Structure getRapidml_structure() {
        return rapidml_structure;
    }

    public void setRapidml_structure(rapidml_Structure rapidml_structure) {
        this.rapidml_structure = rapidml_structure;
    }
    public List<rapidml_Feature> getRapidml_features() {
        return rapidml_features;
    }

    public void addRapidml_feature(Rapidml_feature rapidml_feature) {
        this.rapidml_features.add(rapidml_feature);
    }
    public rapidml_ReferenceElement getRapidml_referenceelement() {
        return rapidml_referenceelement;
    }

    public void setRapidml_referenceelement(rapidml_ReferenceElement rapidml_referenceelement) {
        this.rapidml_referenceelement = rapidml_referenceelement;
    }
    public rapidml_Feature getRapidml_feature() {
        return rapidml_feature;
    }

    public void setRapidml_feature(rapidml_Feature rapidml_feature) {
        this.rapidml_feature = rapidml_feature;
    }

}