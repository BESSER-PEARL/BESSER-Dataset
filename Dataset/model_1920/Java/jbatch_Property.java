





import java.util.List;
import java.util.ArrayList;

public class jbatch_Property  {

    private String name;
    private String value;



    public jbatch_Property(
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


}