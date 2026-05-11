





import java.util.List;
import java.util.ArrayList;

public class adlrecurs_Attributes  {

    private String signature;





    private List<adlrecurs_Attribute> adlrecurs_attributes;




    private adlrecurs_AbstractComponent adlrecurs_abstractcomponent;


    public adlrecurs_Attributes(
        String signature    ) {
        this.signature = signature;
        this.adlrecurs_attributes = new ArrayList<>();
    }

    public adlrecurs_Attributes(
        String signature        ArrayList<adlrecurs_Attribute> adlrecurs_attributes    ) {
        this.signature = signature;
        this.adlrecurs_attributes = adlrecurs_attributes;
    }

    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public List<adlrecurs_Attribute> getAdlrecurs_attributes() {
        return adlrecurs_attributes;
    }

    public void addAdlrecurs_attribute(Adlrecurs_attribute adlrecurs_attribute) {
        this.adlrecurs_attributes.add(adlrecurs_attribute);
    }
    public adlrecurs_AbstractComponent getAdlrecurs_abstractcomponent() {
        return adlrecurs_abstractcomponent;
    }

    public void setAdlrecurs_abstractcomponent(adlrecurs_AbstractComponent adlrecurs_abstractcomponent) {
        this.adlrecurs_abstractcomponent = adlrecurs_abstractcomponent;
    }

}