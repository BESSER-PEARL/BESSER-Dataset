





import java.util.List;
import java.util.ArrayList;

public class Data_Attribute  {

    private String visibility;
    private String name;





    private Data_Class data_class;


    public Data_Attribute(
        String visibility,        String name    ) {
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
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