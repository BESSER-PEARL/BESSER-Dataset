





import java.util.List;
import java.util.ArrayList;

public class modelDsl_CollectionReturnType  {

    private String collection;





    private modelDsl_DefCollectionTypeVariable modeldsl_defcollectiontypevariable;


    public modelDsl_CollectionReturnType(
        String collection    ) {
        this.collection = collection;
    }


    public String getCollection() {
        return collection;
    }

    public void setCollection(String collection) {
        this.collection = collection;
    }

    public modelDsl_DefCollectionTypeVariable getModeldsl_defcollectiontypevariable() {
        return modeldsl_defcollectiontypevariable;
    }

    public void setModeldsl_defcollectiontypevariable(modelDsl_DefCollectionTypeVariable modeldsl_defcollectiontypevariable) {
        this.modeldsl_defcollectiontypevariable = modeldsl_defcollectiontypevariable;
    }

}