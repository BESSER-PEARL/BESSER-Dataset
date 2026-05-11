





import java.util.List;
import java.util.ArrayList;

public class ISO20022_BusinessAttribute extends BusinessElement {






    private ISO20022_DataType iso20022_datatype;




    private ISO20022_BusinessComponent iso20022_businesscomponent;


    public ISO20022_BusinessAttribute(
    ) {
        super(
        );
    }



    public ISO20022_DataType getIso20022_datatype() {
        return iso20022_datatype;
    }

    public void setIso20022_datatype(ISO20022_DataType iso20022_datatype) {
        this.iso20022_datatype = iso20022_datatype;
    }
    public ISO20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(ISO20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}