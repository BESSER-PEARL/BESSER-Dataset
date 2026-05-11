





import java.util.List;
import java.util.ArrayList;

public class Data_Class  {

    private String name;





    private Data_Model data_model;


    public Data_Class(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Data_Model getData_model() {
        return data_model;
    }

    public void setData_model(Data_Model data_model) {
        this.data_model = data_model;
    }

}