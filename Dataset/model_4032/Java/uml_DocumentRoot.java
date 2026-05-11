





import java.util.List;
import java.util.ArrayList;

public class uml_DocumentRoot  {

    private String mixed;





    private List<uml_association> uml_associations;




    private List<uml_attribute> uml_attributes;




    private List<uml_ownerClassifier> uml_ownerclassifiers;




    private List<uml_attributes> uml_attributess;




    private List<uml_primitiveDataType> uml_primitivedatatypes;




    private List<uml_class_> uml_class_s;




    private List<uml_generalClass> uml_generalclasss;




    private List<uml_classifiersAndAssociations> uml_classifiersandassociationss;


    public uml_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.uml_associations = new ArrayList<>();
        this.uml_attributes = new ArrayList<>();
        this.uml_ownerclassifiers = new ArrayList<>();
        this.uml_attributess = new ArrayList<>();
        this.uml_primitivedatatypes = new ArrayList<>();
        this.uml_class_s = new ArrayList<>();
        this.uml_generalclasss = new ArrayList<>();
        this.uml_classifiersandassociationss = new ArrayList<>();
    }

    public uml_DocumentRoot(
        String mixed        ArrayList<uml_association> uml_associations,        ArrayList<uml_attribute> uml_attributes,        ArrayList<uml_ownerClassifier> uml_ownerclassifiers,        ArrayList<uml_attributes> uml_attributess,        ArrayList<uml_primitiveDataType> uml_primitivedatatypes,        ArrayList<uml_class_> uml_class_s,        ArrayList<uml_generalClass> uml_generalclasss,        ArrayList<uml_classifiersAndAssociations> uml_classifiersandassociationss    ) {
        this.mixed = mixed;
        this.uml_associations = uml_associations;
        this.uml_attributes = uml_attributes;
        this.uml_ownerclassifiers = uml_ownerclassifiers;
        this.uml_attributess = uml_attributess;
        this.uml_primitivedatatypes = uml_primitivedatatypes;
        this.uml_class_s = uml_class_s;
        this.uml_generalclasss = uml_generalclasss;
        this.uml_classifiersandassociationss = uml_classifiersandassociationss;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<uml_association> getUml_associations() {
        return uml_associations;
    }

    public void addUml_association(Uml_association uml_association) {
        this.uml_associations.add(uml_association);
    }
    public List<uml_attribute> getUml_attributes() {
        return uml_attributes;
    }

    public void addUml_attribute(Uml_attribute uml_attribute) {
        this.uml_attributes.add(uml_attribute);
    }
    public List<uml_ownerClassifier> getUml_ownerclassifiers() {
        return uml_ownerclassifiers;
    }

    public void addUml_ownerclassifier(Uml_ownerclassifier uml_ownerclassifier) {
        this.uml_ownerclassifiers.add(uml_ownerclassifier);
    }
    public List<uml_attributes> getUml_attributess() {
        return uml_attributess;
    }

    public void addUml_attributes(Uml_attributes uml_attributes) {
        this.uml_attributess.add(uml_attributes);
    }
    public List<uml_primitiveDataType> getUml_primitivedatatypes() {
        return uml_primitivedatatypes;
    }

    public void addUml_primitivedatatype(Uml_primitivedatatype uml_primitivedatatype) {
        this.uml_primitivedatatypes.add(uml_primitivedatatype);
    }
    public List<uml_class_> getUml_class_s() {
        return uml_class_s;
    }

    public void addUml_class_(Uml_class_ uml_class_) {
        this.uml_class_s.add(uml_class_);
    }
    public List<uml_generalClass> getUml_generalclasss() {
        return uml_generalclasss;
    }

    public void addUml_generalclass(Uml_generalclass uml_generalclass) {
        this.uml_generalclasss.add(uml_generalclass);
    }
    public List<uml_classifiersAndAssociations> getUml_classifiersandassociationss() {
        return uml_classifiersandassociationss;
    }

    public void addUml_classifiersandassociations(Uml_classifiersandassociations uml_classifiersandassociations) {
        this.uml_classifiersandassociationss.add(uml_classifiersandassociations);
    }

}