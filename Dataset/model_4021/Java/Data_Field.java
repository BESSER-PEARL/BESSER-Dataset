





import java.util.List;
import java.util.ArrayList;

public class Data_Field  {

    private String type;
    private String modifier;
    private String name;





    private Data_Class data_class;


    public Data_Field(
        String type,        String modifier,        String name    ) {
        this.type = type;
        this.modifier = modifier;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Data_Class getData_class() {
        return data_class;
    }

    public void setData_class(Data_Class data_class) {
        this.data_class = data_class;
    }

}