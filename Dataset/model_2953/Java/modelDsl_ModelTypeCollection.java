





import java.util.List;
import java.util.ArrayList;

public class modelDsl_ModelTypeCollection  {

    private String collection;





    private modelDsl_DefModelModelTypeCollectionVariable modeldsl_defmodelmodeltypecollectionvariable;




    private modelDsl_ModelType modeldsl_modeltype;


    public modelDsl_ModelTypeCollection(
        String collection    ) {
        this.collection = collection;
    }


    public String getCollection() {
        return collection;
    }

    public void setCollection(String collection) {
        this.collection = collection;
    }

    public modelDsl_DefModelModelTypeCollectionVariable getModeldsl_defmodelmodeltypecollectionvariable() {
        return modeldsl_defmodelmodeltypecollectionvariable;
    }

    public void setModeldsl_defmodelmodeltypecollectionvariable(modelDsl_DefModelModelTypeCollectionVariable modeldsl_defmodelmodeltypecollectionvariable) {
        this.modeldsl_defmodelmodeltypecollectionvariable = modeldsl_defmodelmodeltypecollectionvariable;
    }
    public modelDsl_ModelType getModeldsl_modeltype() {
        return modeldsl_modeltype;
    }

    public void setModeldsl_modeltype(modelDsl_ModelType modeldsl_modeltype) {
        this.modeldsl_modeltype = modeldsl_modeltype;
    }

}