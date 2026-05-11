





import java.util.List;
import java.util.ArrayList;

public class Data_Model  {

    private String Name;





    private List<Data_Class> data_classs;


    public Data_Model(
        String Name    ) {
        this.Name = Name;
        this.data_classs = new ArrayList<>();
    }

    public Data_Model(
        String Name        ArrayList<Data_Class> data_classs    ) {
        this.Name = Name;
        this.data_classs = data_classs;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Data_Class> getData_classs() {
        return data_classs;
    }

    public void addData_class(Data_class data_class) {
        this.data_classs.add(data_class);
    }

}