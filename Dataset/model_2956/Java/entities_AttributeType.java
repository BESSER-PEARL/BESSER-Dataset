





import java.util.List;
import java.util.ArrayList;

public class entities_AttributeType  {

    private int length;
    private boolean array;





    private entities_Attribute entities_attribute;


    public entities_AttributeType(
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

    public entities_Attribute getEntities_attribute() {
        return entities_attribute;
    }

    public void setEntities_attribute(entities_Attribute entities_attribute) {
        this.entities_attribute = entities_attribute;
    }

}