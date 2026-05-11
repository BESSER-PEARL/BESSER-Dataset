





import java.util.List;
import java.util.ArrayList;

public class necsis14_classdiagram_ClassDiagram  {






    private List<necsis14_classdiagram_Association> necsis14_classdiagram_associations;




    private List<necsis14_classdiagram_Class> necsis14_classdiagram_classs;


    public necsis14_classdiagram_ClassDiagram(
    ) {
        this.necsis14_classdiagram_associations = new ArrayList<>();
        this.necsis14_classdiagram_classs = new ArrayList<>();
    }

    public necsis14_classdiagram_ClassDiagram(
        ArrayList<necsis14_classdiagram_Association> necsis14_classdiagram_associations,        ArrayList<necsis14_classdiagram_Class> necsis14_classdiagram_classs    ) {
        this.necsis14_classdiagram_associations = necsis14_classdiagram_associations;
        this.necsis14_classdiagram_classs = necsis14_classdiagram_classs;
    }


    public List<necsis14_classdiagram_Association> getNecsis14_classdiagram_associations() {
        return necsis14_classdiagram_associations;
    }

    public void addNecsis14_classdiagram_association(Necsis14_classdiagram_association necsis14_classdiagram_association) {
        this.necsis14_classdiagram_associations.add(necsis14_classdiagram_association);
    }
    public List<necsis14_classdiagram_Class> getNecsis14_classdiagram_classs() {
        return necsis14_classdiagram_classs;
    }

    public void addNecsis14_classdiagram_class(Necsis14_classdiagram_class necsis14_classdiagram_class) {
        this.necsis14_classdiagram_classs.add(necsis14_classdiagram_class);
    }

}