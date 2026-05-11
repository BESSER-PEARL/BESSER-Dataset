





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessComponent extends BusinessElementType, TopLevelDictionaryEntry, BusinessConcept {






    private iso20022_BusinessElement iso20022_businesselement;




    private iso20022_MessageComponentType iso20022_messagecomponenttype;




    private iso20022_BusinessAttribute iso20022_businessattribute;




    private List<iso20022_BusinessComponent> iso20022_businesscomponents;




    private List<iso20022_MessageComponentType> iso20022_messagecomponenttypes;




    private List<iso20022_MessageElement> iso20022_messageelements;




    private iso20022_MessageElement iso20022_messageelement;




    private List<iso20022_BusinessElement> iso20022_businesselements;




    private iso20022_BusinessComponent iso20022_businesscomponent;


    public iso20022_BusinessComponent(
    ) {
        super(
        );
        this.iso20022_businesscomponents = new ArrayList<>();
        this.iso20022_messagecomponenttypes = new ArrayList<>();
        this.iso20022_messageelements = new ArrayList<>();
        this.iso20022_businesselements = new ArrayList<>();
    }

    public iso20022_BusinessComponent(
        ArrayList<iso20022_BusinessComponent> iso20022_businesscomponents,        ArrayList<iso20022_MessageComponentType> iso20022_messagecomponenttypes,        ArrayList<iso20022_MessageElement> iso20022_messageelements,        ArrayList<iso20022_BusinessElement> iso20022_businesselements    ) {
        this.iso20022_businesscomponents = iso20022_businesscomponents;
        this.iso20022_messagecomponenttypes = iso20022_messagecomponenttypes;
        this.iso20022_messageelements = iso20022_messageelements;
        this.iso20022_businesselements = iso20022_businesselements;
    }


    public iso20022_BusinessElement getIso20022_businesselement() {
        return iso20022_businesselement;
    }

    public void setIso20022_businesselement(iso20022_BusinessElement iso20022_businesselement) {
        this.iso20022_businesselement = iso20022_businesselement;
    }
    public iso20022_MessageComponentType getIso20022_messagecomponenttype() {
        return iso20022_messagecomponenttype;
    }

    public void setIso20022_messagecomponenttype(iso20022_MessageComponentType iso20022_messagecomponenttype) {
        this.iso20022_messagecomponenttype = iso20022_messagecomponenttype;
    }
    public iso20022_BusinessAttribute getIso20022_businessattribute() {
        return iso20022_businessattribute;
    }

    public void setIso20022_businessattribute(iso20022_BusinessAttribute iso20022_businessattribute) {
        this.iso20022_businessattribute = iso20022_businessattribute;
    }
    public List<iso20022_BusinessComponent> getIso20022_businesscomponents() {
        return iso20022_businesscomponents;
    }

    public void addIso20022_businesscomponent(Iso20022_businesscomponent iso20022_businesscomponent) {
        this.iso20022_businesscomponents.add(iso20022_businesscomponent);
    }
    public List<iso20022_MessageComponentType> getIso20022_messagecomponenttypes() {
        return iso20022_messagecomponenttypes;
    }

    public void addIso20022_messagecomponenttype(Iso20022_messagecomponenttype iso20022_messagecomponenttype) {
        this.iso20022_messagecomponenttypes.add(iso20022_messagecomponenttype);
    }
    public List<iso20022_MessageElement> getIso20022_messageelements() {
        return iso20022_messageelements;
    }

    public void addIso20022_messageelement(Iso20022_messageelement iso20022_messageelement) {
        this.iso20022_messageelements.add(iso20022_messageelement);
    }
    public iso20022_MessageElement getIso20022_messageelement() {
        return iso20022_messageelement;
    }

    public void setIso20022_messageelement(iso20022_MessageElement iso20022_messageelement) {
        this.iso20022_messageelement = iso20022_messageelement;
    }
    public List<iso20022_BusinessElement> getIso20022_businesselements() {
        return iso20022_businesselements;
    }

    public void addIso20022_businesselement(Iso20022_businesselement iso20022_businesselement) {
        this.iso20022_businesselements.add(iso20022_businesselement);
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}