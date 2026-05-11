





import java.util.List;
import java.util.ArrayList;

public class model_ProductOptions extends IEntity {

    private String attributeValue;
    private String sequenceNumber;



    public model_ProductOptions(
        String attributeValue,        String sequenceNumber    ) {
        super(
        );
        this.attributeValue = attributeValue;
        this.sequenceNumber = sequenceNumber;
    }


    public String getAttributevalue() {
        return attributeValue;
    }

    public void setAttributevalue(String attributeValue) {
        this.attributeValue = attributeValue;
    }
    public String getSequencenumber() {
        return sequenceNumber;
    }

    public void setSequencenumber(String sequenceNumber) {
        this.sequenceNumber = sequenceNumber;
    }


}