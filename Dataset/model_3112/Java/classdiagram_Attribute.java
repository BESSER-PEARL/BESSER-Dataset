





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Attribute  {

    private boolean is_primary;
    private String name;





    private classdiagram_Class classdiagram_class;


    public classdiagram_Attribute(
        boolean is_primary,        String name    ) {
        this.is_primary = is_primary;
        this.name = name;
    }


    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }

}