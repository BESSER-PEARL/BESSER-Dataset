





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessComponent extends TopLevelDictionaryEntry, BusinessConcept, BusinessElementType {






    private List<iso20022_MessageElement> iso20022_messageelements;




    private iso20022_BusinessComponent iso20022_businesscomponent;




    private iso20022_MessageElement iso20022_messageelement;




    private iso20022_BusinessComponent iso20022_businesscomponent;


    public iso20022_BusinessComponent(
    ) {
        super(
        );
        this.iso20022_messageelements = new ArrayList<>();
    }

    public iso20022_BusinessComponent(
        ArrayList<iso20022_MessageElement> iso20022_messageelements    ) {
        this.iso20022_messageelements = iso20022_messageelements;
    }


    public List<iso20022_MessageElement> getIso20022_messageelements() {
        return iso20022_messageelements;
    }

    public void addIso20022_messageelement(Iso20022_messageelement iso20022_messageelement) {
        this.iso20022_messageelements.add(iso20022_messageelement);
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public iso20022_MessageElement getIso20022_messageelement() {
        return iso20022_messageelement;
    }

    public void setIso20022_messageelement(iso20022_MessageElement iso20022_messageelement) {
        this.iso20022_messageelement = iso20022_messageelement;
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}