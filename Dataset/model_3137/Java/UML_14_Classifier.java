





import java.util.List;
import java.util.ArrayList;

public class UML_14_Classifier extends GeneralizableElement, NameSpace {






    private List<UML_14_Parameter> uml_14_parameters;




    private List<UML_14_Generalization> uml_14_generalizations;




    private List<UML_14_Feature> uml_14_features;




    private UML_14_AssociationEnd uml_14_associationend;




    private UML_14_AssociationEnd uml_14_associationend;




    private UML_14_Generalization uml_14_generalization;




    private UML_14_AssociationEnd uml_14_associationend;




    private UML_14_Parameter uml_14_parameter;




    private UML_14_AssociationEnd uml_14_associationend;




    private UML_14_Feature uml_14_feature;


    public UML_14_Classifier(
    ) {
        super(
        );
        this.uml_14_parameters = new ArrayList<>();
        this.uml_14_generalizations = new ArrayList<>();
        this.uml_14_features = new ArrayList<>();
    }

    public UML_14_Classifier(
        ArrayList<UML_14_Parameter> uml_14_parameters,        ArrayList<UML_14_Generalization> uml_14_generalizations,        ArrayList<UML_14_Feature> uml_14_features    ) {
        this.uml_14_parameters = uml_14_parameters;
        this.uml_14_generalizations = uml_14_generalizations;
        this.uml_14_features = uml_14_features;
    }


    public List<UML_14_Parameter> getUml_14_parameters() {
        return uml_14_parameters;
    }

    public void addUml_14_parameter(Uml_14_parameter uml_14_parameter) {
        this.uml_14_parameters.add(uml_14_parameter);
    }
    public List<UML_14_Generalization> getUml_14_generalizations() {
        return uml_14_generalizations;
    }

    public void addUml_14_generalization(Uml_14_generalization uml_14_generalization) {
        this.uml_14_generalizations.add(uml_14_generalization);
    }
    public List<UML_14_Feature> getUml_14_features() {
        return uml_14_features;
    }

    public void addUml_14_feature(Uml_14_feature uml_14_feature) {
        this.uml_14_features.add(uml_14_feature);
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }
    public UML_14_Generalization getUml_14_generalization() {
        return uml_14_generalization;
    }

    public void setUml_14_generalization(UML_14_Generalization uml_14_generalization) {
        this.uml_14_generalization = uml_14_generalization;
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }
    public UML_14_Parameter getUml_14_parameter() {
        return uml_14_parameter;
    }

    public void setUml_14_parameter(UML_14_Parameter uml_14_parameter) {
        this.uml_14_parameter = uml_14_parameter;
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }
    public UML_14_Feature getUml_14_feature() {
        return uml_14_feature;
    }

    public void setUml_14_feature(UML_14_Feature uml_14_feature) {
        this.uml_14_feature = uml_14_feature;
    }

}