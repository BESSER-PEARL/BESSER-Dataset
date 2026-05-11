





import java.util.List;
import java.util.ArrayList;

public class types_Property  {

    private String name;
    private String storageModifier;





    private types_DeclarationTypeReference types_declarationtypereference;




    private types_EntityType types_entitytype;


    public types_Property(
        String name,        String storageModifier    ) {
        this.name = name;
        this.storageModifier = storageModifier;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStoragemodifier() {
        return storageModifier;
    }

    public void setStoragemodifier(String storageModifier) {
        this.storageModifier = storageModifier;
    }

    public types_DeclarationTypeReference getTypes_declarationtypereference() {
        return types_declarationtypereference;
    }

    public void setTypes_declarationtypereference(types_DeclarationTypeReference types_declarationtypereference) {
        this.types_declarationtypereference = types_declarationtypereference;
    }
    public types_EntityType getTypes_entitytype() {
        return types_entitytype;
    }

    public void setTypes_entitytype(types_EntityType types_entitytype) {
        this.types_entitytype = types_entitytype;
    }

}