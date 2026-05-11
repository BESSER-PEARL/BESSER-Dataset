





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_AttributeStringType  {

    private String name;
    private boolean array;
    private int length;



    public ulmDsl2_AttributeStringType(
        String name,        boolean array,        int length    ) {
        this.name = name;
        this.array = array;
        this.length = length;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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