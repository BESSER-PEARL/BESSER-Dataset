





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_EntityFeatureType  {

    private int length;
    private boolean array;





    private ulmDsl2_Entity ulmdsl2_entity;


    public ulmDsl2_EntityFeatureType(
        int length,        boolean array    ) {
        this.length = length;
        this.array = array;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }

    public ulmDsl2_Entity getUlmdsl2_entity() {
        return ulmdsl2_entity;
    }

    public void setUlmdsl2_entity(ulmDsl2_Entity ulmdsl2_entity) {
        this.ulmdsl2_entity = ulmdsl2_entity;
    }

}