





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessAssociationEnd extends BusinessElement {

    private String aggregation;





    private iso20022_BusinessComponent iso20022_businesscomponent;




    private iso20022_BusinessAssociationEnd iso20022_businessassociationend;




    private iso20022_BusinessComponent iso20022_businesscomponent;


    public iso20022_BusinessAssociationEnd(
        String aggregation    ) {
        super(
        );
        this.aggregation = aggregation;
    }


    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }

    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public iso20022_BusinessAssociationEnd getIso20022_businessassociationend() {
        return iso20022_businessassociationend;
    }

    public void setIso20022_businessassociationend(iso20022_BusinessAssociationEnd iso20022_businessassociationend) {
        this.iso20022_businessassociationend = iso20022_businessassociationend;
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}