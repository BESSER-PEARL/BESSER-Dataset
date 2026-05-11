





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Diagram  {






    private List<classdiagram_PrimitiveDataType> classdiagram_primitivedatatypes;




    private List<classdiagram_Class> classdiagram_classs;


    public classdiagram_Diagram(
    ) {
        this.classdiagram_primitivedatatypes = new ArrayList<>();
        this.classdiagram_classs = new ArrayList<>();
    }

    public classdiagram_Diagram(
        ArrayList<classdiagram_PrimitiveDataType> classdiagram_primitivedatatypes,        ArrayList<classdiagram_Class> classdiagram_classs    ) {
        this.classdiagram_primitivedatatypes = classdiagram_primitivedatatypes;
        this.classdiagram_classs = classdiagram_classs;
    }


    public List<classdiagram_PrimitiveDataType> getClassdiagram_primitivedatatypes() {
        return classdiagram_primitivedatatypes;
    }

    public void addClassdiagram_primitivedatatype(Classdiagram_primitivedatatype classdiagram_primitivedatatype) {
        this.classdiagram_primitivedatatypes.add(classdiagram_primitivedatatype);
    }
    public List<classdiagram_Class> getClassdiagram_classs() {
        return classdiagram_classs;
    }

    public void addClassdiagram_class(Classdiagram_class classdiagram_class) {
        this.classdiagram_classs.add(classdiagram_class);
    }

}