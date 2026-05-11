





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Interface  {

    private String name;





    private List<classdiagram_Attribute> classdiagram_attributes;




    private List<classdiagram_Method> classdiagram_methods;


    public classdiagram_Interface(
        String name    ) {
        this.name = name;
        this.classdiagram_attributes = new ArrayList<>();
        this.classdiagram_methods = new ArrayList<>();
    }

    public classdiagram_Interface(
        String name        ArrayList<classdiagram_Attribute> classdiagram_attributes,        ArrayList<classdiagram_Method> classdiagram_methods    ) {
        this.name = name;
        this.classdiagram_attributes = classdiagram_attributes;
        this.classdiagram_methods = classdiagram_methods;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<classdiagram_Attribute> getClassdiagram_attributes() {
        return classdiagram_attributes;
    }

    public void addClassdiagram_attribute(Classdiagram_attribute classdiagram_attribute) {
        this.classdiagram_attributes.add(classdiagram_attribute);
    }
    public List<classdiagram_Method> getClassdiagram_methods() {
        return classdiagram_methods;
    }

    public void addClassdiagram_method(Classdiagram_method classdiagram_method) {
        this.classdiagram_methods.add(classdiagram_method);
    }

}