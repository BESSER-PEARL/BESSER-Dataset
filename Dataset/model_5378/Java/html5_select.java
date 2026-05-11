





import java.util.List;
import java.util.ArrayList;

public class html5_select extends htmlElement {

    private String multiple;
    private String size;



    public html5_select(
        String multiple,        String size    ) {
        super(
        );
        this.multiple = multiple;
        this.size = size;
    }


    public String getMultiple() {
        return multiple;
    }

    public void setMultiple(String multiple) {
        this.multiple = multiple;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}