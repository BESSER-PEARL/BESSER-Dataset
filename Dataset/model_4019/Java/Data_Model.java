





import java.util.List;
import java.util.ArrayList;

public class Data_Model  {






    private List<Data_Classe> data_classes;


    public Data_Model(
    ) {
        this.data_classes = new ArrayList<>();
    }

    public Data_Model(
        ArrayList<Data_Classe> data_classes    ) {
        this.data_classes = data_classes;
    }


    public List<Data_Classe> getData_classes() {
        return data_classes;
    }

    public void addData_classe(Data_classe data_classe) {
        this.data_classes.add(data_classe);
    }

}