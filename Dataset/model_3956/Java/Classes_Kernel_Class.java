





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Class extends Classifier {






    private List<Property> propertys;


    public Classes_Kernel_Class(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
    }

    public Classes_Kernel_Class(
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