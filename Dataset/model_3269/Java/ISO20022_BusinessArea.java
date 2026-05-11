





import java.util.List;
import java.util.ArrayList;

public class ISO20022_BusinessArea extends TopLevelCatalogueEntry {

    private String code;





    private ISO20022_MessageDefinition iso20022_messagedefinition;




    private List<ISO20022_MessageDefinition> iso20022_messagedefinitions;


    public ISO20022_BusinessArea(
        String code    ) {
        super(
        );
        this.code = code;
        this.iso20022_messagedefinitions = new ArrayList<>();
    }

    public ISO20022_BusinessArea(
        String code        ArrayList<ISO20022_MessageDefinition> iso20022_messagedefinitions    ) {
        this.code = code;
        this.iso20022_messagedefinitions = iso20022_messagedefinitions;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public ISO20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(ISO20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }
    public List<ISO20022_MessageDefinition> getIso20022_messagedefinitions() {
        return iso20022_messagedefinitions;
    }

    public void addIso20022_messagedefinition(Iso20022_messagedefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinitions.add(iso20022_messagedefinition);
    }

}