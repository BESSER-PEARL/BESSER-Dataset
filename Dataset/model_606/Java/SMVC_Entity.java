





import java.util.List;
import java.util.ArrayList;

public class SMVC_Entity  {

    private String name;





    private SMVC_EntityComponent smvc_entitycomponent;




    private SMVC_SMVCApplication smvc_smvcapplication;




    private SMVC_DataAccessObject smvc_dataaccessobject;




    private List<SMVC_Attribute> smvc_attributes;




    private SMVC_Attribute smvc_attribute;


    public SMVC_Entity(
        String name    ) {
        this.name = name;
        this.smvc_attributes = new ArrayList<>();
    }

    public SMVC_Entity(
        String name        ArrayList<SMVC_Attribute> smvc_attributes    ) {
        this.name = name;
        this.smvc_attributes = smvc_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SMVC_EntityComponent getSmvc_entitycomponent() {
        return smvc_entitycomponent;
    }

    public void setSmvc_entitycomponent(SMVC_EntityComponent smvc_entitycomponent) {
        this.smvc_entitycomponent = smvc_entitycomponent;
    }
    public SMVC_SMVCApplication getSmvc_smvcapplication() {
        return smvc_smvcapplication;
    }

    public void setSmvc_smvcapplication(SMVC_SMVCApplication smvc_smvcapplication) {
        this.smvc_smvcapplication = smvc_smvcapplication;
    }
    public SMVC_DataAccessObject getSmvc_dataaccessobject() {
        return smvc_dataaccessobject;
    }

    public void setSmvc_dataaccessobject(SMVC_DataAccessObject smvc_dataaccessobject) {
        this.smvc_dataaccessobject = smvc_dataaccessobject;
    }
    public List<SMVC_Attribute> getSmvc_attributes() {
        return smvc_attributes;
    }

    public void addSmvc_attribute(Smvc_attribute smvc_attribute) {
        this.smvc_attributes.add(smvc_attribute);
    }
    public SMVC_Attribute getSmvc_attribute() {
        return smvc_attribute;
    }

    public void setSmvc_attribute(SMVC_Attribute smvc_attribute) {
        this.smvc_attribute = smvc_attribute;
    }

}