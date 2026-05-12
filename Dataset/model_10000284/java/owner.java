





import java.util.List;
import java.util.ArrayList;

public class owner  {






    private List<Property> propertys;


    public owner(
    ) {
        this.propertys = new ArrayList<>();
    }

    public owner(
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