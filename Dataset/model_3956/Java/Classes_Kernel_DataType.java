





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_DataType extends Classifier {






    private List<Property> propertys;


    public Classes_Kernel_DataType(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
    }

    public Classes_Kernel_DataType(
        ArrayList<Property> propertys    ) {
        this.propertys = propertys;
    }


    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}