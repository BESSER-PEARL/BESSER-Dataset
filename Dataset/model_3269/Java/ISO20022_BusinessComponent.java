





import java.util.List;
import java.util.ArrayList;

public class ISO20022_BusinessComponent extends BusinessConcept, BusinessElementType, TopLevelDictionaryEntry {

    private String previousVersionDocumentation;





    private ISO20022_BusinessComponent iso20022_businesscomponent;




    private ISO20022_MessageComponentType iso20022_messagecomponenttype;




    private List<ISO20022_MessageComponentType> iso20022_messagecomponenttypes;




    private ISO20022_BusinessComponent iso20022_businesscomponent;


    public ISO20022_BusinessComponent(
        String previousVersionDocumentation    ) {
        super(
        );
        this.previousVersionDocumentation = previousVersionDocumentation;
        this.iso20022_messagecomponenttypes = new ArrayList<>();
    }

    public ISO20022_BusinessComponent(
        String previousVersionDocumentation        ArrayList<ISO20022_MessageComponentType> iso20022_messagecomponenttypes    ) {
        this.previousVersionDocumentation = previousVersionDocumentation;
        this.iso20022_messagecomponenttypes = iso20022_messagecomponenttypes;
    }

    public String getPreviousversiondocumentation() {
        return previousVersionDocumentation;
    }

    public void setPreviousversiondocumentation(String previousVersionDocumentation) {
        this.previousVersionDocumentation = previousVersionDocumentation;
    }

    public ISO20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(ISO20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public ISO20022_MessageComponentType getIso20022_messagecomponenttype() {
        return iso20022_messagecomponenttype;
    }

    public void setIso20022_messagecomponenttype(ISO20022_MessageComponentType iso20022_messagecomponenttype) {
        this.iso20022_messagecomponenttype = iso20022_messagecomponenttype;
    }
    public List<ISO20022_MessageComponentType> getIso20022_messagecomponenttypes() {
        return iso20022_messagecomponenttypes;
    }

    public void addIso20022_messagecomponenttype(Iso20022_messagecomponenttype iso20022_messagecomponenttype) {
        this.iso20022_messagecomponenttypes.add(iso20022_messagecomponenttype);
    }
    public ISO20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(ISO20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}