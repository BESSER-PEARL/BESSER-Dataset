





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CollectionTypeCS extends cst_SimpleNameCS, cst_TypeCS {

    private String collectionTypeIdentifier;





    private TypeCS typecs;


    public ocl_cst_CollectionTypeCS(
        String collectionTypeIdentifier    ) {
        super(
        );
        this.collectionTypeIdentifier = collectionTypeIdentifier;
    }


    public String getCollectiontypeidentifier() {
        return collectionTypeIdentifier;
    }

    public void setCollectiontypeidentifier(String collectionTypeIdentifier) {
        this.collectionTypeIdentifier = collectionTypeIdentifier;
    }

    public TypeCS getTypecs() {
        return typecs;
    }

    public void setTypecs(TypeCS typecs) {
        this.typecs = typecs;
    }

}