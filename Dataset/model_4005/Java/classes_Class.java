





import java.util.List;
import java.util.ArrayList;

public class classes_Class extends NamedElement {






    private classes_Package classes_package;




    private classes_Class classes_class;


    public classes_Class(
    ) {
        super(
        );
    }



    public classes_Package getClasses_package() {
        return classes_package;
    }

    public void setClasses_package(classes_Package classes_package) {
        this.classes_package = classes_package;
    }
    public classes_Class getClasses_class() {
        return classes_class;
    }

    public void setClasses_class(classes_Class classes_class) {
        this.classes_class = classes_class;
    }

}