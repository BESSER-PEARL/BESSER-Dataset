





import java.util.List;
import java.util.ArrayList;

public class model_Type  {

    private String typeName;
    private int typeId;





    private model_CollectionType model_collectiontype;




    private model_MOperation model_moperation;




    private model_MAttribute model_mattribute;


    public model_Type(
        String typeName,        int typeId    ) {
        this.typeName = typeName;
        this.typeId = typeId;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public int getTypeid() {
        return typeId;
    }

    public void setTypeid(int typeId) {
        this.typeId = typeId;
    }

    public model_CollectionType getModel_collectiontype() {
        return model_collectiontype;
    }

    public void setModel_collectiontype(model_CollectionType model_collectiontype) {
        this.model_collectiontype = model_collectiontype;
    }
    public model_MOperation getModel_moperation() {
        return model_moperation;
    }

    public void setModel_moperation(model_MOperation model_moperation) {
        this.model_moperation = model_moperation;
    }
    public model_MAttribute getModel_mattribute() {
        return model_mattribute;
    }

    public void setModel_mattribute(model_MAttribute model_mattribute) {
        this.model_mattribute = model_mattribute;
    }

}