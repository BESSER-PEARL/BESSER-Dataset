





import java.util.List;
import java.util.ArrayList;

public class org_structure_UnresolvedProperty extends structure_UnresolvedReference, structure_AbstractProperty {

    private String propertyIdentifier;



    public org_structure_UnresolvedProperty(
        String propertyIdentifier    ) {
        super(
        );
        this.propertyIdentifier = propertyIdentifier;
    }


    public String getPropertyidentifier() {
        return propertyIdentifier;
    }

    public void setPropertyidentifier(String propertyIdentifier) {
        this.propertyIdentifier = propertyIdentifier;
    }


}