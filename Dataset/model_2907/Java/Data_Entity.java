





import java.util.List;
import java.util.ArrayList;

public class Data_Entity extends Type {






    private List<Data_Attribute> data_attributes;


    public Data_Entity(
    ) {
        super(
        );
        this.data_attributes = new ArrayList<>();
    }

    public Data_Entity(
        ArrayList<Data_Attribute> data_attributes    ) {
        this.data_attributes = data_attributes;
    }


    public List<Data_Attribute> getData_attributes() {
        return data_attributes;
    }

    public void addData_attribute(Data_attribute data_attribute) {
        this.data_attributes.add(data_attribute);
    }

}