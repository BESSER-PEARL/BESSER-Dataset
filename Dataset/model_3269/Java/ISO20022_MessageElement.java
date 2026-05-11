





import java.util.List;
import java.util.ArrayList;

public class ISO20022_MessageElement extends MessageConcept, XMLMember {

    private boolean isDerived;
    private boolean isTechnical;
    private String tracePath;





    private ISO20022_BusinessElement iso20022_businesselement;




    private ISO20022_MessageElementContainer iso20022_messageelementcontainer;




    private ISO20022_BusinessComponent iso20022_businesscomponent;




    private ISO20022_BusinessElement iso20022_businesselement;




    private ISO20022_BusinessComponent iso20022_businesscomponent;




    private ISO20022_MessageElementContainer iso20022_messageelementcontainer;


    public ISO20022_MessageElement(
        boolean isDerived,        boolean isTechnical,        String tracePath    ) {
        super(
        );
        this.isDerived = isDerived;
        this.isTechnical = isTechnical;
        this.tracePath = tracePath;
    }


    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIstechnical() {
        return isTechnical;
    }

    public void setIstechnical(boolean isTechnical) {
        this.isTechnical = isTechnical;
    }
    public String getTracepath() {
        return tracePath;
    }

    public void setTracepath(String tracePath) {
        this.tracePath = tracePath;
    }

    public ISO20022_BusinessElement getIso20022_businesselement() {
        return iso20022_businesselement;
    }

    public void setIso20022_businesselement(ISO20022_BusinessElement iso20022_businesselement) {
        this.iso20022_businesselement = iso20022_businesselement;
    }
    public ISO20022_MessageElementContainer getIso20022_messageelementcontainer() {
        return iso20022_messageelementcontainer;
    }

    public void setIso20022_messageelementcontainer(ISO20022_MessageElementContainer iso20022_messageelementcontainer) {
        this.iso20022_messageelementcontainer = iso20022_messageelementcontainer;
    }
    public ISO20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(ISO20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public ISO20022_BusinessElement getIso20022_businesselement() {
        return iso20022_businesselement;
    }

    public void setIso20022_businesselement(ISO20022_BusinessElement iso20022_businesselement) {
        this.iso20022_businesselement = iso20022_businesselement;
    }
    public ISO20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(ISO20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public ISO20022_MessageElementContainer getIso20022_messageelementcontainer() {
        return iso20022_messageelementcontainer;
    }

    public void setIso20022_messageelementcontainer(ISO20022_MessageElementContainer iso20022_messageelementcontainer) {
        this.iso20022_messageelementcontainer = iso20022_messageelementcontainer;
    }

}