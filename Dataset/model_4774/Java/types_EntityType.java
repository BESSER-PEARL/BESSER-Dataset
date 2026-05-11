





import java.util.List;
import java.util.ArrayList;

public class types_EntityType extends ComplexType {

    private String storageModifier;



    public types_EntityType(
        String storageModifier    ) {
        super(
        );
        this.storageModifier = storageModifier;
    }


    public String getStoragemodifier() {
        return storageModifier;
    }

    public void setStoragemodifier(String storageModifier) {
        this.storageModifier = storageModifier;
    }


}