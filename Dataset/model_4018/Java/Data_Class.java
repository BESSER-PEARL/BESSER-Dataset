





import java.util.List;
import java.util.ArrayList;

public class Data_Class  {

    private String Name;





    private Data_Model data_model;


    public Data_Class(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Data_Model getData_model() {
        return data_model;
    }

    public void setData_model(Data_Model data_model) {
        this.data_model = data_model;
    }

}