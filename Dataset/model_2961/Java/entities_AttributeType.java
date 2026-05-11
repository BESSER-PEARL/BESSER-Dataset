





import java.util.List;
import java.util.ArrayList;

public class entities_AttributeType  {

    private boolean array;
    private int length;





    private entities_Attribute entities_attribute;


    public entities_AttributeType(
        boolean array,        int length    ) {
        this.array = array;
        this.length = length;
    }


    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public entities_Attribute getEntities_attribute() {
        return entities_attribute;
    }

    public void setEntities_attribute(entities_Attribute entities_attribute) {
        this.entities_attribute = entities_attribute;
    }

}