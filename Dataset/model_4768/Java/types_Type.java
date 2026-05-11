





import java.util.List;
import java.util.ArrayList;

public class types_Type  {

    private boolean mayBeUndefined;
    private boolean multivalued;
    private String metamodelRef;





    private types_TupleAttribute types_tupleattribute;




    private types_Type types_type;




    private types_MapType types_maptype;




    private types_MapType types_maptype;


    public types_Type(
        boolean mayBeUndefined,        boolean multivalued,        String metamodelRef    ) {
        this.mayBeUndefined = mayBeUndefined;
        this.multivalued = multivalued;
        this.metamodelRef = metamodelRef;
    }


    public boolean getMaybeundefined() {
        return mayBeUndefined;
    }

    public void setMaybeundefined(boolean mayBeUndefined) {
        this.mayBeUndefined = mayBeUndefined;
    }
    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }
    public String getMetamodelref() {
        return metamodelRef;
    }

    public void setMetamodelref(String metamodelRef) {
        this.metamodelRef = metamodelRef;
    }

    public types_TupleAttribute getTypes_tupleattribute() {
        return types_tupleattribute;
    }

    public void setTypes_tupleattribute(types_TupleAttribute types_tupleattribute) {
        this.types_tupleattribute = types_tupleattribute;
    }
    public types_Type getTypes_type() {
        return types_type;
    }

    public void setTypes_type(types_Type types_type) {
        this.types_type = types_type;
    }
    public types_MapType getTypes_maptype() {
        return types_maptype;
    }

    public void setTypes_maptype(types_MapType types_maptype) {
        this.types_maptype = types_maptype;
    }
    public types_MapType getTypes_maptype() {
        return types_maptype;
    }

    public void setTypes_maptype(types_MapType types_maptype) {
        this.types_maptype = types_maptype;
    }

}