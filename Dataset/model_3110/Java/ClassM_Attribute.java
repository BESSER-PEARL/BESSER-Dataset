





import java.util.List;
import java.util.ArrayList;

public class ClassM_Attribute  {

    private String name;
    private boolean is_primary;





    private ClassM_Class classm_class;




    private ClassM_Class classm_class;


    public ClassM_Attribute(
        String name,        boolean is_primary    ) {
        this.name = name;
        this.is_primary = is_primary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }

    public ClassM_Class getClassm_class() {
        return classm_class;
    }

    public void setClassm_class(ClassM_Class classm_class) {
        this.classm_class = classm_class;
    }
    public ClassM_Class getClassm_class() {
        return classm_class;
    }

    public void setClassm_class(ClassM_Class classm_class) {
        this.classm_class = classm_class;
    }

}