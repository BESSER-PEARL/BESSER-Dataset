





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageBuildingBlock extends MessageConstruct {






    private iso20022_MessageDefinition iso20022_messagedefinition;




    private iso20022_Xor iso20022_xor;


    public iso20022_MessageBuildingBlock(
    ) {
        super(
        );
    }



    public iso20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(iso20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }
    public iso20022_Xor getIso20022_xor() {
        return iso20022_xor;
    }

    public void setIso20022_xor(iso20022_Xor iso20022_xor) {
        this.iso20022_xor = iso20022_xor;
    }

}