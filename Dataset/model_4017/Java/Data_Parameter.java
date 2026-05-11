





import java.util.List;
import java.util.ArrayList;

public class Data_Parameter  {

    private String name;
    private String type;





    private Data_Method data_method;


    public Data_Parameter(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Data_Method getData_method() {
        return data_method;
    }

    public void setData_method(Data_Method data_method) {
        this.data_method = data_method;
    }

}