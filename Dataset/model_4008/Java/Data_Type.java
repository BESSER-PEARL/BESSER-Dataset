





import java.util.List;
import java.util.ArrayList;

public class Data_Type  {

    private String name;
    private boolean isReference;





    private Data_Attribute data_attribute;


    public Data_Type(
        String name,        boolean isReference    ) {
        this.name = name;
        this.isReference = isReference;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsreference() {
        return isReference;
    }

    public void setIsreference(boolean isReference) {
        this.isReference = isReference;
    }

    public Data_Attribute getData_attribute() {
        return data_attribute;
    }

    public void setData_attribute(Data_Attribute data_attribute) {
        this.data_attribute = data_attribute;
    }

}