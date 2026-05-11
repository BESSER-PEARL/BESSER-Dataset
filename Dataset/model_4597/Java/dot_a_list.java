





import java.util.List;
import java.util.ArrayList;

public class dot_a_list  {

    private String name;
    private String value;





    private dot_attr_list dot_attr_list;


    public dot_a_list(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public dot_attr_list getDot_attr_list() {
        return dot_attr_list;
    }

    public void setDot_attr_list(dot_attr_list dot_attr_list) {
        this.dot_attr_list = dot_attr_list;
    }

}