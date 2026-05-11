





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Class extends Classifier {






    private uml2CD_Classifier uml2cd_classifier;




    private uml2CD_Property uml2cd_property;




    private List<uml2CD_Property> uml2cd_propertys;




    private List<uml2CD_Class> uml2cd_classs;




    private List<uml2CD_Classifier> uml2cd_classifiers;


    public uml2CD_Class(
    ) {
        super(
        );
        this.uml2cd_propertys = new ArrayList<>();
        this.uml2cd_classs = new ArrayList<>();
        this.uml2cd_classifiers = new ArrayList<>();
    }

    public uml2CD_Class(
        ArrayList<uml2CD_Property> uml2cd_propertys,        ArrayList<uml2CD_Class> uml2cd_classs,        ArrayList<uml2CD_Classifier> uml2cd_classifiers    ) {
        this.uml2cd_propertys = uml2cd_propertys;
        this.uml2cd_classs = uml2cd_classs;
        this.uml2cd_classifiers = uml2cd_classifiers;
    }


    public uml2CD_Classifier getUml2cd_classifier() {
        return uml2cd_classifier;
    }

    public void setUml2cd_classifier(uml2CD_Classifier uml2cd_classifier) {
        this.uml2cd_classifier = uml2cd_classifier;
    }
    public uml2CD_Property getUml2cd_property() {
        return uml2cd_property;
    }

    public void setUml2cd_property(uml2CD_Property uml2cd_property) {
        this.uml2cd_property = uml2cd_property;
    }
    public List<uml2CD_Property> getUml2cd_propertys() {
        return uml2cd_propertys;
    }

    public void addUml2cd_property(Uml2cd_property uml2cd_property) {
        this.uml2cd_propertys.add(uml2cd_property);
    }
    public List<uml2CD_Class> getUml2cd_classs() {
        return uml2cd_classs;
    }

    public void addUml2cd_class(Uml2cd_class uml2cd_class) {
        this.uml2cd_classs.add(uml2cd_class);
    }
    public List<uml2CD_Classifier> getUml2cd_classifiers() {
        return uml2cd_classifiers;
    }

    public void addUml2cd_classifier(Uml2cd_classifier uml2cd_classifier) {
        this.uml2cd_classifiers.add(uml2cd_classifier);
    }

}