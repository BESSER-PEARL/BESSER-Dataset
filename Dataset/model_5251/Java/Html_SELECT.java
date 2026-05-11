





import java.util.List;
import java.util.ArrayList;

public class Html_SELECT  {

    private String multiple;
    private String name;
    private String size;



    public Html_SELECT(
        String multiple,        String name,        String size    ) {
        this.multiple = multiple;
        this.name = name;
        this.size = size;
    }


    public String getMultiple() {
        return multiple;
    }

    public void setMultiple(String multiple) {
        this.multiple = multiple;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}