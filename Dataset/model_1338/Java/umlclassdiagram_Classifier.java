





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Classifier extends Modifier {

    private boolean abstract;
    private boolean derived;





    private umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram;




    private List<umlclassdiagram_Feature> umlclassdiagram_features;


    public umlclassdiagram_Classifier(
        boolean abstract,        boolean derived    ) {
        super(
        );
        this.abstract = abstract;
        this.derived = derived;
        this.umlclassdiagram_features = new ArrayList<>();
    }

    public umlclassdiagram_Classifier(
        boolean abstract,        boolean derived        ArrayList<umlclassdiagram_Feature> umlclassdiagram_features    ) {
        this.abstract = abstract;
        this.derived = derived;
        this.umlclassdiagram_features = umlclassdiagram_features;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }

    public umlclassdiagram_ClassDiagram getUmlclassdiagram_classdiagram() {
        return umlclassdiagram_classdiagram;
    }

    public void setUmlclassdiagram_classdiagram(umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram) {
        this.umlclassdiagram_classdiagram = umlclassdiagram_classdiagram;
    }
    public List<umlclassdiagram_Feature> getUmlclassdiagram_features() {
        return umlclassdiagram_features;
    }

    public void addUmlclassdiagram_feature(Umlclassdiagram_feature umlclassdiagram_feature) {
        this.umlclassdiagram_features.add(umlclassdiagram_feature);
    }

}