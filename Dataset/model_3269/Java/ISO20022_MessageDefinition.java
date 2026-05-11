





import java.util.List;
import java.util.ArrayList;

public class ISO20022_MessageDefinition extends Type {

    private String urn;
    private String xmlTag;
    private String previousVersionDocumentation;
    private String visibility;
    private String rootElement;
    private String xmlName;





    private ISO20022_Xor iso20022_xor;




    private List<ISO20022_Xor> iso20022_xors;




    private List<ISO20022_MessageBuildingBlock> iso20022_messagebuildingblocks;




    private ISO20022_MessageDefinition iso20022_messagedefinition;




    private ISO20022_MessageDefinition iso20022_messagedefinition;


    public ISO20022_MessageDefinition(
        String urn,        String xmlTag,        String previousVersionDocumentation,        String visibility,        String rootElement,        String xmlName    ) {
        super(
        );
        this.urn = urn;
        this.xmlTag = xmlTag;
        this.previousVersionDocumentation = previousVersionDocumentation;
        this.visibility = visibility;
        this.rootElement = rootElement;
        this.xmlName = xmlName;
        this.iso20022_xors = new ArrayList<>();
        this.iso20022_messagebuildingblocks = new ArrayList<>();
    }

    public ISO20022_MessageDefinition(
        String urn,        String xmlTag,        String previousVersionDocumentation,        String visibility,        String rootElement,        String xmlName        ArrayList<ISO20022_Xor> iso20022_xors,        ArrayList<ISO20022_MessageBuildingBlock> iso20022_messagebuildingblocks    ) {
        this.urn = urn;
        this.xmlTag = xmlTag;
        this.previousVersionDocumentation = previousVersionDocumentation;
        this.visibility = visibility;
        this.rootElement = rootElement;
        this.xmlName = xmlName;
        this.iso20022_xors = iso20022_xors;
        this.iso20022_messagebuildingblocks = iso20022_messagebuildingblocks;
    }

    public String getUrn() {
        return urn;
    }

    public void setUrn(String urn) {
        this.urn = urn;
    }
    public String getXmltag() {
        return xmlTag;
    }

    public void setXmltag(String xmlTag) {
        this.xmlTag = xmlTag;
    }
    public String getPreviousversiondocumentation() {
        return previousVersionDocumentation;
    }

    public void setPreviousversiondocumentation(String previousVersionDocumentation) {
        this.previousVersionDocumentation = previousVersionDocumentation;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getRootelement() {
        return rootElement;
    }

    public void setRootelement(String rootElement) {
        this.rootElement = rootElement;
    }
    public String getXmlname() {
        return xmlName;
    }

    public void setXmlname(String xmlName) {
        this.xmlName = xmlName;
    }

    public ISO20022_Xor getIso20022_xor() {
        return iso20022_xor;
    }

    public void setIso20022_xor(ISO20022_Xor iso20022_xor) {
        this.iso20022_xor = iso20022_xor;
    }
    public List<ISO20022_Xor> getIso20022_xors() {
        return iso20022_xors;
    }

    public void addIso20022_xor(Iso20022_xor iso20022_xor) {
        this.iso20022_xors.add(iso20022_xor);
    }
    public List<ISO20022_MessageBuildingBlock> getIso20022_messagebuildingblocks() {
        return iso20022_messagebuildingblocks;
    }

    public void addIso20022_messagebuildingblock(Iso20022_messagebuildingblock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblocks.add(iso20022_messagebuildingblock);
    }
    public ISO20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(ISO20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }
    public ISO20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(ISO20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }

}