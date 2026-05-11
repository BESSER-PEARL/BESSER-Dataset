





import java.util.List;
import java.util.ArrayList;

public class Class_Class extends Classifier {

    private boolean isAbstract;





    private List<Class> classs;




    private List<Attribute> attributes;


    public Class_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.classs = new ArrayList<>();
        this.attributes = new ArrayList<>();
    }

    public Class_Class(
        boolean isAbstract        ArrayList<Class> classs,        ArrayList<Attribute> attributes    ) {
        this.isAbstract = isAbstract;
        this.classs = classs;
        this.attributes = attributes;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<Class> getClasss() {
        return classs;
    }

    public void addClass(Class class) {
        this.classs.add(class);
    }
    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }

}