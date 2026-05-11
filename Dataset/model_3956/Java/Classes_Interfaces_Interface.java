





import java.util.List;
import java.util.ArrayList;

public class Classes_Interfaces_Interface extends Classifier {






    private List<Property> propertys;


    public Classes_Interfaces_Interface(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
    }

    public Classes_Interfaces_Interface(
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