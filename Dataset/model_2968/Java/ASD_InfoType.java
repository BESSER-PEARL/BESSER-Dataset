





import java.util.List;
import java.util.ArrayList;

public class ASD_InfoType extends NamedElement {

    private String valueType;
    private String valueRange;
    private String subset;





    private List<ASD_Message> asd_messages;




    private List<ASD_InfoType> asd_infotypes;




    private ASD_InfoType asd_infotype;




    private ASD_Message asd_message;




    private ASD_ServiceDescription asd_servicedescription;




    private ASD_ServiceDescription asd_servicedescription;


    public ASD_InfoType(
        String valueType,        String valueRange,        String subset    ) {
        super(
        );
        this.valueType = valueType;
        this.valueRange = valueRange;
        this.subset = subset;
        this.asd_messages = new ArrayList<>();
        this.asd_infotypes = new ArrayList<>();
    }

    public ASD_InfoType(
        String valueType,        String valueRange,        String subset        ArrayList<ASD_Message> asd_messages,        ArrayList<ASD_InfoType> asd_infotypes    ) {
        this.valueType = valueType;
        this.valueRange = valueRange;
        this.subset = subset;
        this.asd_messages = asd_messages;
        this.asd_infotypes = asd_infotypes;
    }

    public String getValuetype() {
        return valueType;
    }

    public void setValuetype(String valueType) {
        this.valueType = valueType;
    }
    public String getValuerange() {
        return valueRange;
    }

    public void setValuerange(String valueRange) {
        this.valueRange = valueRange;
    }
    public String getSubset() {
        return subset;
    }

    public void setSubset(String subset) {
        this.subset = subset;
    }

    public List<ASD_Message> getAsd_messages() {
        return asd_messages;
    }

    public void addAsd_message(Asd_message asd_message) {
        this.asd_messages.add(asd_message);
    }
    public List<ASD_InfoType> getAsd_infotypes() {
        return asd_infotypes;
    }

    public void addAsd_infotype(Asd_infotype asd_infotype) {
        this.asd_infotypes.add(asd_infotype);
    }
    public ASD_InfoType getAsd_infotype() {
        return asd_infotype;
    }

    public void setAsd_infotype(ASD_InfoType asd_infotype) {
        this.asd_infotype = asd_infotype;
    }
    public ASD_Message getAsd_message() {
        return asd_message;
    }

    public void setAsd_message(ASD_Message asd_message) {
        this.asd_message = asd_message;
    }
    public ASD_ServiceDescription getAsd_servicedescription() {
        return asd_servicedescription;
    }

    public void setAsd_servicedescription(ASD_ServiceDescription asd_servicedescription) {
        this.asd_servicedescription = asd_servicedescription;
    }
    public ASD_ServiceDescription getAsd_servicedescription() {
        return asd_servicedescription;
    }

    public void setAsd_servicedescription(ASD_ServiceDescription asd_servicedescription) {
        this.asd_servicedescription = asd_servicedescription;
    }

}