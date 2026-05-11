





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Property extends StructuralFeature {

    private String default;
    private boolean isDerived;
    private boolean isComposite;
    private boolean isID;
    private boolean isDerivedUnion;





    private ClassesProv_Interface classesprov_interface;




    private ClassesProv_Property classesprov_property;




    private ClassesProv_Property classesprov_property;




    private ClassesProv_Association classesprov_association;




    private ClassesProv_Classifier classesprov_classifier;




    private ClassesProv_Association classesprov_association;




    private ClassesProv_DataType classesprov_datatype;




    private ClassesProv_Association classesprov_association;




    private ClassesProv_Property classesprov_property;




    private ClassesProv_Property classesprov_property;




    private ClassesProv_Association classesprov_association;




    private ClassesProv_Interface classesprov_interface;




    private ClassesProv_ValueSpecification classesprov_valuespecification;




    private ClassesProv_Association classesprov_association;




    private List<ClassesProv_Property> classesprov_propertys;




    private ClassesProv_DataType classesprov_datatype;


    public ClassesProv_Property(
        String default,        boolean isDerived,        boolean isComposite,        boolean isID,        boolean isDerivedUnion    ) {
        super(
        );
        this.default = default;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.isID = isID;
        this.isDerivedUnion = isDerivedUnion;
        this.classesprov_propertys = new ArrayList<>();
    }

    public ClassesProv_Property(
        String default,        boolean isDerived,        boolean isComposite,        boolean isID,        boolean isDerivedUnion        ArrayList<ClassesProv_Property> classesprov_propertys    ) {
        this.default = default;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.isID = isID;
        this.isDerivedUnion = isDerivedUnion;
        this.classesprov_propertys = classesprov_propertys;
    }

    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIsid() {
        return isID;
    }

    public void setIsid(boolean isID) {
        this.isID = isID;
    }
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }

    public ClassesProv_Interface getClassesprov_interface() {
        return classesprov_interface;
    }

    public void setClassesprov_interface(ClassesProv_Interface classesprov_interface) {
        this.classesprov_interface = classesprov_interface;
    }
    public ClassesProv_Property getClassesprov_property() {
        return classesprov_property;
    }

    public void setClassesprov_property(ClassesProv_Property classesprov_property) {
        this.classesprov_property = classesprov_property;
    }
    public ClassesProv_Property getClassesprov_property() {
        return classesprov_property;
    }

    public void setClassesprov_property(ClassesProv_Property classesprov_property) {
        this.classesprov_property = classesprov_property;
    }
    public ClassesProv_Association getClassesprov_association() {
        return classesprov_association;
    }

    public void setClassesprov_association(ClassesProv_Association classesprov_association) {
        this.classesprov_association = classesprov_association;
    }
    public ClassesProv_Classifier getClassesprov_classifier() {
        return classesprov_classifier;
    }

    public void setClassesprov_classifier(ClassesProv_Classifier classesprov_classifier) {
        this.classesprov_classifier = classesprov_classifier;
    }
    public ClassesProv_Association getClassesprov_association() {
        return classesprov_association;
    }

    public void setClassesprov_association(ClassesProv_Association classesprov_association) {
        this.classesprov_association = classesprov_association;
    }
    public ClassesProv_DataType getClassesprov_datatype() {
        return classesprov_datatype;
    }

    public void setClassesprov_datatype(ClassesProv_DataType classesprov_datatype) {
        this.classesprov_datatype = classesprov_datatype;
    }
    public ClassesProv_Association getClassesprov_association() {
        return classesprov_association;
    }

    public void setClassesprov_association(ClassesProv_Association classesprov_association) {
        this.classesprov_association = classesprov_association;
    }
    public ClassesProv_Property getClassesprov_property() {
        return classesprov_property;
    }

    public void setClassesprov_property(ClassesProv_Property classesprov_property) {
        this.classesprov_property = classesprov_property;
    }
    public ClassesProv_Property getClassesprov_property() {
        return classesprov_property;
    }

    public void setClassesprov_property(ClassesProv_Property classesprov_property) {
        this.classesprov_property = classesprov_property;
    }
    public ClassesProv_Association getClassesprov_association() {
        return classesprov_association;
    }

    public void setClassesprov_association(ClassesProv_Association classesprov_association) {
        this.classesprov_association = classesprov_association;
    }
    public ClassesProv_Interface getClassesprov_interface() {
        return classesprov_interface;
    }

    public void setClassesprov_interface(ClassesProv_Interface classesprov_interface) {
        this.classesprov_interface = classesprov_interface;
    }
    public ClassesProv_ValueSpecification getClassesprov_valuespecification() {
        return classesprov_valuespecification;
    }

    public void setClassesprov_valuespecification(ClassesProv_ValueSpecification classesprov_valuespecification) {
        this.classesprov_valuespecification = classesprov_valuespecification;
    }
    public ClassesProv_Association getClassesprov_association() {
        return classesprov_association;
    }

    public void setClassesprov_association(ClassesProv_Association classesprov_association) {
        this.classesprov_association = classesprov_association;
    }
    public List<ClassesProv_Property> getClassesprov_propertys() {
        return classesprov_propertys;
    }

    public void addClassesprov_property(Classesprov_property classesprov_property) {
        this.classesprov_propertys.add(classesprov_property);
    }
    public ClassesProv_DataType getClassesprov_datatype() {
        return classesprov_datatype;
    }

    public void setClassesprov_datatype(ClassesProv_DataType classesprov_datatype) {
        this.classesprov_datatype = classesprov_datatype;
    }

}