





import java.util.List;
import java.util.ArrayList;

public class classes_Attribute  {

    private String name;
    private String value;





    private classes_Class classes_class;




    private classes_Type classes_type;


    public classes_Attribute(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public classes_Class getClasses_class() {
        return classes_class;
    }

    public void setClasses_class(classes_Class classes_class) {
        this.classes_class = classes_class;
    }
    public classes_Type getClasses_type() {
        return classes_type;
    }

    public void setClasses_type(classes_Type classes_type) {
        this.classes_type = classes_type;
    }

}