





import java.util.List;
import java.util.ArrayList;

public class iso20022_DataType extends TopLevelDictionaryEntry, BusinessElementType, LogicalType {






    private iso20022_Amount iso20022_amount;




    private iso20022_MessageBuildingBlock iso20022_messagebuildingblock;


    public iso20022_DataType(
    ) {
        super(
        );
    }



    public iso20022_Amount getIso20022_amount() {
        return iso20022_amount;
    }

    public void setIso20022_amount(iso20022_Amount iso20022_amount) {
        this.iso20022_amount = iso20022_amount;
    }
    public iso20022_MessageBuildingBlock getIso20022_messagebuildingblock() {
        return iso20022_messagebuildingblock;
    }

    public void setIso20022_messagebuildingblock(iso20022_MessageBuildingBlock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblock = iso20022_messagebuildingblock;
    }

}