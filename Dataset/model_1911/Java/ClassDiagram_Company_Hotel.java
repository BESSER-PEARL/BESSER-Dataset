





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Company_Hotel  {

    private String name;





    private ClassDiagram_Company classdiagram_company;


    public ClassDiagram_Company_Hotel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_Company getClassdiagram_company() {
        return classdiagram_company;
    }

    public void setClassdiagram_company(ClassDiagram_Company classdiagram_company) {
        this.classdiagram_company = classdiagram_company;
    }

}