





import java.util.List;
import java.util.ArrayList;

public class Data_Attribute  {

    private String type;
    private String encapsulation;
    private String name;





    private Data_Class data_class;


    public Data_Attribute(
        String type,        String encapsulation,        String name    ) {
        this.type = type;
        this.encapsulation = encapsulation;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getEncapsulation() {
        return encapsulation;
    }

    public void setEncapsulation(String encapsulation) {
        this.encapsulation = encapsulation;
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