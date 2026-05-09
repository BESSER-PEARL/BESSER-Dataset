





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_OperationalTransformation extends Module {






    private List<Property> propertys;




    private List<Class> classs;




    private Transformation transformation;


    public qvtoperational_OperationalTransformation(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
        this.classs = new ArrayList<>();
    }

    public qvtoperational_OperationalTransformation(
        ArrayList<Property> propertys,        ArrayList<Class> classs    ) {
        this.propertys = propertys;
        this.classs = classs;
    }


    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }
    public List<Class> getClasss() {
        return classs;
    }

    public void addClass(Class class) {
        this.classs.add(class);
    }
    public Transformation getTransformation() {
        return transformation;
    }

    public void setTransformation(Transformation transformation) {
        this.transformation = transformation;
    }

}