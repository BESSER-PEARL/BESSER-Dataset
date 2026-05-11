





import java.util.List;
import java.util.ArrayList;

public class html_SELECT  {

    private String size;
    private String multiple;
    private String name;



    public html_SELECT(
        String size,        String multiple,        String name    ) {
        this.size = size;
        this.multiple = multiple;
        this.name = name;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
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


}