





import java.util.List;
import java.util.ArrayList;

public class classes_Attribute extends Description {

    private String visibility;
    private String name;





    private classes_Class classes_class;


    public classes_Attribute(
        String visibility,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classes_Class getClasses_class() {
        return classes_class;
    }

    public void setClasses_class(classes_Class classes_class) {
        this.classes_class = classes_class;
    }

}