





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Relation extends Modifier {

    private String ntar;
    private boolean derived;
    private String nsrc;





    private umlclassdiagram_Classifier umlclassdiagram_classifier;




    private umlclassdiagram_Classifier umlclassdiagram_classifier;




    private umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram;


    public umlclassdiagram_Relation(
        String ntar,        boolean derived,        String nsrc    ) {
        super(
        );
        this.ntar = ntar;
        this.derived = derived;
        this.nsrc = nsrc;
    }


    public String getNtar() {
        return ntar;
    }

    public void setNtar(String ntar) {
        this.ntar = ntar;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public String getNsrc() {
        return nsrc;
    }

    public void setNsrc(String nsrc) {
        this.nsrc = nsrc;
    }

    public umlclassdiagram_Classifier getUmlclassdiagram_classifier() {
        return umlclassdiagram_classifier;
    }

    public void setUmlclassdiagram_classifier(umlclassdiagram_Classifier umlclassdiagram_classifier) {
        this.umlclassdiagram_classifier = umlclassdiagram_classifier;
    }
    public umlclassdiagram_Classifier getUmlclassdiagram_classifier() {
        return umlclassdiagram_classifier;
    }

    public void setUmlclassdiagram_classifier(umlclassdiagram_Classifier umlclassdiagram_classifier) {
        this.umlclassdiagram_classifier = umlclassdiagram_classifier;
    }
    public umlclassdiagram_ClassDiagram getUmlclassdiagram_classdiagram() {
        return umlclassdiagram_classdiagram;
    }

    public void setUmlclassdiagram_classdiagram(umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram) {
        this.umlclassdiagram_classdiagram = umlclassdiagram_classdiagram;
    }

}