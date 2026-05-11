





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Diagram  {






    private List<classdiagram_PrimitiveDataType> classdiagram_primitivedatatypes;




    private List<classdiagram_Class> classdiagram_classs;




    private List<classdiagram_Generalization> classdiagram_generalizations;




    private List<classdiagram_Association> classdiagram_associations;


    public classdiagram_Diagram(
    ) {
        this.classdiagram_primitivedatatypes = new ArrayList<>();
        this.classdiagram_classs = new ArrayList<>();
        this.classdiagram_generalizations = new ArrayList<>();
        this.classdiagram_associations = new ArrayList<>();
    }

    public classdiagram_Diagram(
        ArrayList<classdiagram_PrimitiveDataType> classdiagram_primitivedatatypes,        ArrayList<classdiagram_Class> classdiagram_classs,        ArrayList<classdiagram_Generalization> classdiagram_generalizations,        ArrayList<classdiagram_Association> classdiagram_associations    ) {
        this.classdiagram_primitivedatatypes = classdiagram_primitivedatatypes;
        this.classdiagram_classs = classdiagram_classs;
        this.classdiagram_generalizations = classdiagram_generalizations;
        this.classdiagram_associations = classdiagram_associations;
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
    public List<classdiagram_Generalization> getClassdiagram_generalizations() {
        return classdiagram_generalizations;
    }

    public void addClassdiagram_generalization(Classdiagram_generalization classdiagram_generalization) {
        this.classdiagram_generalizations.add(classdiagram_generalization);
    }
    public List<classdiagram_Association> getClassdiagram_associations() {
        return classdiagram_associations;
    }

    public void addClassdiagram_association(Classdiagram_association classdiagram_association) {
        this.classdiagram_associations.add(classdiagram_association);
    }

}