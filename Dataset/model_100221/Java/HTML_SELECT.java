





import java.util.List;
import java.util.ArrayList;

public class HTML_SELECT  {

    private String size;
    private String name;
    private String multiple;



    public HTML_SELECT(
        String size,        String name,        String multiple    ) {
        this.size = size;
        this.name = name;
        this.multiple = multiple;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMultiple() {
        return multiple;
    }

    public void setMultiple(String multiple) {
        this.multiple = multiple;
    }


}