





import java.util.List;
import java.util.ArrayList;

public class entities_AttributeType  {

    private boolean array;
    private int length;



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


}