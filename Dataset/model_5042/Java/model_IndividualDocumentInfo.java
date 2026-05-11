





import java.util.List;
import java.util.ArrayList;

public class model_IndividualDocumentInfo extends IEntity {

    private String shippingAutoVat;
    private String shippingDescription;
    private String shippingValue;
    private String noVatName;
    private String paymentDescription;
    private String paymentName;
    private String paymentText;
    private String shippingVatValue;
    private String shippingName;
    private String noVatDescription;
    private String shippingVatDescription;



    public model_IndividualDocumentInfo(
        String shippingAutoVat,        String shippingDescription,        String shippingValue,        String noVatName,        String paymentDescription,        String paymentName,        String paymentText,        String shippingVatValue,        String shippingName,        String noVatDescription,        String shippingVatDescription    ) {
        super(
        );
        this.shippingAutoVat = shippingAutoVat;
        this.shippingDescription = shippingDescription;
        this.shippingValue = shippingValue;
        this.noVatName = noVatName;
        this.paymentDescription = paymentDescription;
        this.paymentName = paymentName;
        this.paymentText = paymentText;
        this.shippingVatValue = shippingVatValue;
        this.shippingName = shippingName;
        this.noVatDescription = noVatDescription;
        this.shippingVatDescription = shippingVatDescription;
    }


    public String getShippingautovat() {
        return shippingAutoVat;
    }

    public void setShippingautovat(String shippingAutoVat) {
        this.shippingAutoVat = shippingAutoVat;
    }
    public String getShippingdescription() {
        return shippingDescription;
    }

    public void setShippingdescription(String shippingDescription) {
        this.shippingDescription = shippingDescription;
    }
    public String getShippingvalue() {
        return shippingValue;
    }

    public void setShippingvalue(String shippingValue) {
        this.shippingValue = shippingValue;
    }
    public String getNovatname() {
        return noVatName;
    }

    public void setNovatname(String noVatName) {
        this.noVatName = noVatName;
    }
    public String getPaymentdescription() {
        return paymentDescription;
    }

    public void setPaymentdescription(String paymentDescription) {
        this.paymentDescription = paymentDescription;
    }
    public String getPaymentname() {
        return paymentName;
    }

    public void setPaymentname(String paymentName) {
        this.paymentName = paymentName;
    }
    public String getPaymenttext() {
        return paymentText;
    }

    public void setPaymenttext(String paymentText) {
        this.paymentText = paymentText;
    }
    public String getShippingvatvalue() {
        return shippingVatValue;
    }

    public void setShippingvatvalue(String shippingVatValue) {
        this.shippingVatValue = shippingVatValue;
    }
    public String getShippingname() {
        return shippingName;
    }

    public void setShippingname(String shippingName) {
        this.shippingName = shippingName;
    }
    public String getNovatdescription() {
        return noVatDescription;
    }

    public void setNovatdescription(String noVatDescription) {
        this.noVatDescription = noVatDescription;
    }
    public String getShippingvatdescription() {
        return shippingVatDescription;
    }

    public void setShippingvatdescription(String shippingVatDescription) {
        this.shippingVatDescription = shippingVatDescription;
    }


}