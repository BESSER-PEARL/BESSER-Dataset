





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_VersionProperty  {

    private String name;
    private String value;



    public esmodel_versioning_VersionProperty(
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