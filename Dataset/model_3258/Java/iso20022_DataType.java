





import java.util.List;
import java.util.ArrayList;

public class iso20022_DataType extends LogicalType, TopLevelDictionaryEntry, BusinessElementType {






    private iso20022_BusinessAttribute iso20022_businessattribute;




    private iso20022_MessageBuildingBlock iso20022_messagebuildingblock;




    private iso20022_Amount iso20022_amount;




    private iso20022_MessageAttribute iso20022_messageattribute;


    public iso20022_DataType(
    ) {
        super(
        );
    }



    public iso20022_BusinessAttribute getIso20022_businessattribute() {
        return iso20022_businessattribute;
    }

    public void setIso20022_businessattribute(iso20022_BusinessAttribute iso20022_businessattribute) {
        this.iso20022_businessattribute = iso20022_businessattribute;
    }
    public iso20022_MessageBuildingBlock getIso20022_messagebuildingblock() {
        return iso20022_messagebuildingblock;
    }

    public void setIso20022_messagebuildingblock(iso20022_MessageBuildingBlock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblock = iso20022_messagebuildingblock;
    }
    public iso20022_Amount getIso20022_amount() {
        return iso20022_amount;
    }

    public void setIso20022_amount(iso20022_Amount iso20022_amount) {
        this.iso20022_amount = iso20022_amount;
    }
    public iso20022_MessageAttribute getIso20022_messageattribute() {
        return iso20022_messageattribute;
    }

    public void setIso20022_messageattribute(iso20022_MessageAttribute iso20022_messageattribute) {
        this.iso20022_messageattribute = iso20022_messageattribute;
    }

}