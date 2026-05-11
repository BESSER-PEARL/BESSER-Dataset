





import java.util.List;
import java.util.ArrayList;

public class umlMM__Package  {

    private String name;





    private List<umlMM__Association> umlmm__associations;




    private umlMM__dummy umlmm__dummy;




    private umlMM__Association umlmm__association;




    private List<umlMM__Classifier> umlmm__classifiers;




    private umlMM__dummy umlmm__dummy;




    private umlMM__Classifier umlmm__classifier;


    public umlMM__Package(
        String name    ) {
        this.name = name;
        this.umlmm__associations = new ArrayList<>();
        this.umlmm__classifiers = new ArrayList<>();
    }

    public umlMM__Package(
        String name        ArrayList<umlMM__Association> umlmm__associations,        ArrayList<umlMM__Classifier> umlmm__classifiers    ) {
        this.name = name;
        this.umlmm__associations = umlmm__associations;
        this.umlmm__classifiers = umlmm__classifiers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<umlMM__Association> getUmlmm__associations() {
        return umlmm__associations;
    }

    public void addUmlmm__association(Umlmm__association umlmm__association) {
        this.umlmm__associations.add(umlmm__association);
    }
    public umlMM__dummy getUmlmm__dummy() {
        return umlmm__dummy;
    }

    public void setUmlmm__dummy(umlMM__dummy umlmm__dummy) {
        this.umlmm__dummy = umlmm__dummy;
    }
    public umlMM__Association getUmlmm__association() {
        return umlmm__association;
    }

    public void setUmlmm__association(umlMM__Association umlmm__association) {
        this.umlmm__association = umlmm__association;
    }
    public List<umlMM__Classifier> getUmlmm__classifiers() {
        return umlmm__classifiers;
    }

    public void addUmlmm__classifier(Umlmm__classifier umlmm__classifier) {
        this.umlmm__classifiers.add(umlmm__classifier);
    }
    public umlMM__dummy getUmlmm__dummy() {
        return umlmm__dummy;
    }

    public void setUmlmm__dummy(umlMM__dummy umlmm__dummy) {
        this.umlmm__dummy = umlmm__dummy;
    }
    public umlMM__Classifier getUmlmm__classifier() {
        return umlmm__classifier;
    }

    public void setUmlmm__classifier(umlMM__Classifier umlmm__classifier) {
        this.umlmm__classifier = umlmm__classifier;
    }

}