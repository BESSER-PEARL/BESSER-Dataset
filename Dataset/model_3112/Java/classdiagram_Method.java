





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Method  {

    private String name;





    private classdiagram_Class classdiagram_class;


    public classdiagram_Method(
        String name    ) {
        this.name = name;
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