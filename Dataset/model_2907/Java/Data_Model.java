





import java.util.List;
import java.util.ArrayList;

public class Data_Model  {






    private List<Data_Type> data_types;


    public Data_Model(
    ) {
        this.data_types = new ArrayList<>();
    }

    public Data_Model(
        ArrayList<Data_Type> data_types    ) {
        this.data_types = data_types;
    }


    public List<Data_Type> getData_types() {
        return data_types;
    }

    public void addData_type(Data_type data_type) {
        this.data_types.add(data_type);
    }

}