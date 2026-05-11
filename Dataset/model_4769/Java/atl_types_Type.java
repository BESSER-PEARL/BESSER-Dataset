





import java.util.List;
import java.util.ArrayList;

public class atl_types_Type  {

    private boolean multivalued;





    private atl_types_MapType atl_types_maptype;




    private atl_types_MapType atl_types_maptype;




    private atl_types_TupleAttribute atl_types_tupleattribute;




    private atl_types_UnionType atl_types_uniontype;


    public atl_types_Type(
        boolean multivalued    ) {
        this.multivalued = multivalued;
    }


    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }

    public atl_types_MapType getAtl_types_maptype() {
        return atl_types_maptype;
    }

    public void setAtl_types_maptype(atl_types_MapType atl_types_maptype) {
        this.atl_types_maptype = atl_types_maptype;
    }
    public atl_types_MapType getAtl_types_maptype() {
        return atl_types_maptype;
    }

    public void setAtl_types_maptype(atl_types_MapType atl_types_maptype) {
        this.atl_types_maptype = atl_types_maptype;
    }
    public atl_types_TupleAttribute getAtl_types_tupleattribute() {
        return atl_types_tupleattribute;
    }

    public void setAtl_types_tupleattribute(atl_types_TupleAttribute atl_types_tupleattribute) {
        this.atl_types_tupleattribute = atl_types_tupleattribute;
    }
    public atl_types_UnionType getAtl_types_uniontype() {
        return atl_types_uniontype;
    }

    public void setAtl_types_uniontype(atl_types_UnionType atl_types_uniontype) {
        this.atl_types_uniontype = atl_types_uniontype;
    }

}