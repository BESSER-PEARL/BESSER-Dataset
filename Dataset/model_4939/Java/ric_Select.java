





import java.util.List;
import java.util.ArrayList;

public class ric_Select extends FormControl {

    private int size;
    private boolean multiple;



    public ric_Select(
        int size,        boolean multiple    ) {
        super(
        );
        this.size = size;
        this.multiple = multiple;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }


}