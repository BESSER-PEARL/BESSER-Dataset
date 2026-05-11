





import java.util.List;
import java.util.ArrayList;

public class Data_Attribute  {

    private String Name;
    private String Type;





    private Data_Class data_class;


    public Data_Attribute(
        String Name,        String Type    ) {
        this.Name = Name;
        this.Type = Type;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public Data_Class getData_class() {
        return data_class;
    }

    public void setData_class(Data_Class data_class) {
        this.data_class = data_class;
    }

}