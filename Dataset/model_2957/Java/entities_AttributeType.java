





import java.util.List;
import java.util.ArrayList;

public class entities_AttributeType  {

    private int lenght;
    private boolean array;



    public entities_AttributeType(
        int lenght,        boolean array    ) {
        this.lenght = lenght;
        this.array = array;
    }


    public int getLenght() {
        return lenght;
    }

    public void setLenght(int lenght) {
        this.lenght = lenght;
    }
    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }


}