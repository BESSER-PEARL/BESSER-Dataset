





import java.util.List;
import java.util.ArrayList;

public class carnot_DataType extends ITypedElement, IIdentifiableModelElement {

    private String predefined;





    private List<carnot_ParameterMappingType> carnot_parametermappingtypes;




    private carnot_ModelType carnot_modeltype;




    private List<carnot_DataMappingType> carnot_datamappingtypes;




    private carnot_DataMappingType carnot_datamappingtype;




    private carnot_ParameterMappingType carnot_parametermappingtype;


    public carnot_DataType(
        String predefined    ) {
        super(
        );
        this.predefined = predefined;
        this.carnot_parametermappingtypes = new ArrayList<>();
        this.carnot_datamappingtypes = new ArrayList<>();
    }

    public carnot_DataType(
        String predefined        ArrayList<carnot_ParameterMappingType> carnot_parametermappingtypes,        ArrayList<carnot_DataMappingType> carnot_datamappingtypes    ) {
        this.predefined = predefined;
        this.carnot_parametermappingtypes = carnot_parametermappingtypes;
        this.carnot_datamappingtypes = carnot_datamappingtypes;
    }

    public String getPredefined() {
        return predefined;
    }

    public void setPredefined(String predefined) {
        this.predefined = predefined;
    }

    public List<carnot_ParameterMappingType> getCarnot_parametermappingtypes() {
        return carnot_parametermappingtypes;
    }

    public void addCarnot_parametermappingtype(Carnot_parametermappingtype carnot_parametermappingtype) {
        this.carnot_parametermappingtypes.add(carnot_parametermappingtype);
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public List<carnot_DataMappingType> getCarnot_datamappingtypes() {
        return carnot_datamappingtypes;
    }

    public void addCarnot_datamappingtype(Carnot_datamappingtype carnot_datamappingtype) {
        this.carnot_datamappingtypes.add(carnot_datamappingtype);
    }
    public carnot_DataMappingType getCarnot_datamappingtype() {
        return carnot_datamappingtype;
    }

    public void setCarnot_datamappingtype(carnot_DataMappingType carnot_datamappingtype) {
        this.carnot_datamappingtype = carnot_datamappingtype;
    }
    public carnot_ParameterMappingType getCarnot_parametermappingtype() {
        return carnot_parametermappingtype;
    }

    public void setCarnot_parametermappingtype(carnot_ParameterMappingType carnot_parametermappingtype) {
        this.carnot_parametermappingtype = carnot_parametermappingtype;
    }

}