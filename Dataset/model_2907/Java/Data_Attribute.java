





import java.util.List;
import java.util.ArrayList;

public class Data_Attribute  {

    private String name;





    private Data_Type data_type;


    public Data_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Data_Type getData_type() {
        return data_type;
    }

    public void setData_type(Data_Type data_type) {
        this.data_type = data_type;
    }

}