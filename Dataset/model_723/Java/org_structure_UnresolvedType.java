





import java.util.List;
import java.util.ArrayList;

public class org_structure_UnresolvedType extends structure_Type, structure_UnresolvedReference, structure_TypeContainer {

    private String typeIdentifier;



    public org_structure_UnresolvedType(
        String typeIdentifier    ) {
        super(
        );
        this.typeIdentifier = typeIdentifier;
    }


    public String getTypeidentifier() {
        return typeIdentifier;
    }

    public void setTypeidentifier(String typeIdentifier) {
        this.typeIdentifier = typeIdentifier;
    }


}