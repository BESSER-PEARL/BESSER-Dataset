





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CollectionLiteralExpCS extends LiteralExpCS {

    private String collectionType;



    public ocl_cst_CollectionLiteralExpCS(
        String collectionType    ) {
        super(
        );
        this.collectionType = collectionType;
    }


    public String getCollectiontype() {
        return collectionType;
    }

    public void setCollectiontype(String collectionType) {
        this.collectionType = collectionType;
    }


}