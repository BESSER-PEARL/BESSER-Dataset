





import java.util.List;
import java.util.ArrayList;

public class Ant_Attribut  {

    private String value;
    private String name;



    public Ant_Attribut(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}