





import java.util.List;
import java.util.ArrayList;

public class ric_Select extends FormControl {

    private boolean multiple;
    private int size;



    public ric_Select(
        boolean multiple,        int size    ) {
        super(
        );
        this.multiple = multiple;
        this.size = size;
    }


    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}