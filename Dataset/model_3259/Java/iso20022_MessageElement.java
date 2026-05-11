





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageElement extends MessageConcept, MessageConstruct {

    private boolean isTechnical;
    private boolean isDerived;





    private iso20022_Xor iso20022_xor;




    private iso20022_MessageElementContainer iso20022_messageelementcontainer;




    private iso20022_BusinessElement iso20022_businesselement;




    private iso20022_BusinessComponent iso20022_businesscomponent;




    private iso20022_BusinessElement iso20022_businesselement;




    private iso20022_MessageElementContainer iso20022_messageelementcontainer;




    private iso20022_BusinessComponent iso20022_businesscomponent;


    public iso20022_MessageElement(
        boolean isTechnical,        boolean isDerived    ) {
        super(
        );
        this.isTechnical = isTechnical;
        this.isDerived = isDerived;
    }


    public boolean getIstechnical() {
        return isTechnical;
    }

    public void setIstechnical(boolean isTechnical) {
        this.isTechnical = isTechnical;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }

    public iso20022_Xor getIso20022_xor() {
        return iso20022_xor;
    }

    public void setIso20022_xor(iso20022_Xor iso20022_xor) {
        this.iso20022_xor = iso20022_xor;
    }
    public iso20022_MessageElementContainer getIso20022_messageelementcontainer() {
        return iso20022_messageelementcontainer;
    }

    public void setIso20022_messageelementcontainer(iso20022_MessageElementContainer iso20022_messageelementcontainer) {
        this.iso20022_messageelementcontainer = iso20022_messageelementcontainer;
    }
    public iso20022_BusinessElement getIso20022_businesselement() {
        return iso20022_businesselement;
    }

    public void setIso20022_businesselement(iso20022_BusinessElement iso20022_businesselement) {
        this.iso20022_businesselement = iso20022_businesselement;
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public iso20022_BusinessElement getIso20022_businesselement() {
        return iso20022_businesselement;
    }

    public void setIso20022_businesselement(iso20022_BusinessElement iso20022_businesselement) {
        this.iso20022_businesselement = iso20022_businesselement;
    }
    public iso20022_MessageElementContainer getIso20022_messageelementcontainer() {
        return iso20022_messageelementcontainer;
    }

    public void setIso20022_messageelementcontainer(iso20022_MessageElementContainer iso20022_messageelementcontainer) {
        this.iso20022_messageelementcontainer = iso20022_messageelementcontainer;
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}