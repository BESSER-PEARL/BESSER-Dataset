





import java.util.List;
import java.util.ArrayList;

public class Data_Method  {

    private String name;
    private String modifier;
    private String type;





    private Data_Class data_class;


    public Data_Method(
        String name,        String modifier,        String type    ) {
        this.name = name;
        this.modifier = modifier;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Data_Class getData_class() {
        return data_class;
    }

    public void setData_class(Data_Class data_class) {
        this.data_class = data_class;
    }

}