





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_OperationalTransformation extends Module {






    private List<Class> classs;




    private List<Property> propertys;


    public QVTOperational_OperationalTransformation(
    ) {
        super(
        );
        this.classs = new ArrayList<>();
        this.propertys = new ArrayList<>();
    }

    public QVTOperational_OperationalTransformation(
        ArrayList<Class> classs,        ArrayList<Property> propertys    ) {
        this.classs = classs;
        this.propertys = propertys;
    }


    public List<Class> getClasss() {
        return classs;
    }

    public void addClass(Class class) {
        this.classs.add(class);
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}