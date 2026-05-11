





import java.util.List;
import java.util.ArrayList;

public class ISO20022_SyntaxMessageScheme extends TopLevelCatalogueEntry {






    private List<ISO20022_MessageDefinition> iso20022_messagedefinitions;




    private ISO20022_MessageDefinition iso20022_messagedefinition;


    public ISO20022_SyntaxMessageScheme(
    ) {
        super(
        );
        this.iso20022_messagedefinitions = new ArrayList<>();
    }

    public ISO20022_SyntaxMessageScheme(
        ArrayList<ISO20022_MessageDefinition> iso20022_messagedefinitions    ) {
        this.iso20022_messagedefinitions = iso20022_messagedefinitions;
    }


    public List<ISO20022_MessageDefinition> getIso20022_messagedefinitions() {
        return iso20022_messagedefinitions;
    }

    public void addIso20022_messagedefinition(Iso20022_messagedefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinitions.add(iso20022_messagedefinition);
    }
    public ISO20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(ISO20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }

}