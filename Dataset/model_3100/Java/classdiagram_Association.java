





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Association  {

    private String name;





    private classdiagram_Package classdiagram_package;


    public classdiagram_Association(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classdiagram_Package getClassdiagram_package() {
        return classdiagram_package;
    }

    public void setClassdiagram_package(classdiagram_Package classdiagram_package) {
        this.classdiagram_package = classdiagram_package;
    }

}