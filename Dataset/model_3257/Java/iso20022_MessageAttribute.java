





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageAttribute extends MessageElement {






    private iso20022_MessageComponentType iso20022_messagecomponenttype;




    private iso20022_DataType iso20022_datatype;


    public iso20022_MessageAttribute(
    ) {
        super(
        );
    }



    public iso20022_MessageComponentType getIso20022_messagecomponenttype() {
        return iso20022_messagecomponenttype;
    }

    public void setIso20022_messagecomponenttype(iso20022_MessageComponentType iso20022_messagecomponenttype) {
        this.iso20022_messagecomponenttype = iso20022_messagecomponenttype;
    }
    public iso20022_DataType getIso20022_datatype() {
        return iso20022_datatype;
    }

    public void setIso20022_datatype(iso20022_DataType iso20022_datatype) {
        this.iso20022_datatype = iso20022_datatype;
    }

}