





import java.util.List;
import java.util.ArrayList;

public class QVTRelation_Key extends Element {






    private List<Property> propertys;




    private Class class;




    private List<Property> propertys;


    public QVTRelation_Key(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
        this.propertys = new ArrayList<>();
    }

    public QVTRelation_Key(
        ArrayList<Property> propertys,        ArrayList<Property> propertys    ) {
        this.propertys = propertys;
        this.propertys = propertys;
    }


    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}