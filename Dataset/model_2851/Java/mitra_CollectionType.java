





import java.util.List;
import java.util.ArrayList;

public class mitra_CollectionType extends Type {

    private String collectionType;





    private mitra_Type mitra_type;


    public mitra_CollectionType(
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

    public mitra_Type getMitra_type() {
        return mitra_type;
    }

    public void setMitra_type(mitra_Type mitra_type) {
        this.mitra_type = mitra_type;
    }

}