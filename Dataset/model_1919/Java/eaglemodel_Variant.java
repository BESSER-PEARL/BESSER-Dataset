





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Variant  {

    private String technology;
    private boolean populate;
    private String value;
    private String name;



    public eaglemodel_Variant(
        String technology,        boolean populate,        String value,        String name    ) {
        this.technology = technology;
        this.populate = populate;
        this.value = value;
        this.name = name;
    }


    public String getTechnology() {
        return technology;
    }

    public void setTechnology(String technology) {
        this.technology = technology;
    }
    public boolean getPopulate() {
        return populate;
    }

    public void setPopulate(boolean populate) {
        this.populate = populate;
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