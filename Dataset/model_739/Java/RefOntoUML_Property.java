





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Property extends StructuralFeature {

    private String isComposite;
    private String default;
    private String isDerived;
    private String isDerivedUnion;
    private String aggregation;





    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_Property refontouml_property;




    private RefOntoUML_DataType refontouml_datatype;




    private RefOntoUML_ValueSpecification refontouml_valuespecification;




    private RefOntoUML_Class refontouml_class;




    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_Property refontouml_property;




    private List<RefOntoUML_Property> refontouml_propertys;




    private RefOntoUML_Class refontouml_class;




    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_DataType refontouml_datatype;




    private RefOntoUML_Classifier refontouml_classifier;


    public RefOntoUML_Property(
        String isComposite,        String default,        String isDerived,        String isDerivedUnion,        String aggregation    ) {
        super(
        );
        this.isComposite = isComposite;
        this.default = default;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.refontouml_propertys = new ArrayList<>();
    }

    public RefOntoUML_Property(
        String isComposite,        String default,        String isDerived,        String isDerivedUnion,        String aggregation        ArrayList<RefOntoUML_Property> refontouml_propertys    ) {
        this.isComposite = isComposite;
        this.default = default;
        this.isDerived = isDerived;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.refontouml_propertys = refontouml_propertys;
    }

    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(String isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }

    public RefOntoUML_Association getRefontouml_association() {
        return refontouml_association;
    }

    public void setRefontouml_association(RefOntoUML_Association refontouml_association) {
        this.refontouml_association = refontouml_association;
    }
    public RefOntoUML_Property getRefontouml_property() {
        return refontouml_property;
    }

    public void setRefontouml_property(RefOntoUML_Property refontouml_property) {
        this.refontouml_property = refontouml_property;
    }
    public RefOntoUML_DataType getRefontouml_datatype() {
        return refontouml_datatype;
    }

    public void setRefontouml_datatype(RefOntoUML_DataType refontouml_datatype) {
        this.refontouml_datatype = refontouml_datatype;
    }
    public RefOntoUML_ValueSpecification getRefontouml_valuespecification() {
        return refontouml_valuespecification;
    }

    public void setRefontouml_valuespecification(RefOntoUML_ValueSpecification refontouml_valuespecification) {
        this.refontouml_valuespecification = refontouml_valuespecification;
    }
    public RefOntoUML_Class getRefontouml_class() {
        return refontouml_class;
    }

    public void setRefontouml_class(RefOntoUML_Class refontouml_class) {
        this.refontouml_class = refontouml_class;
    }
    public RefOntoUML_Association getRefontouml_association() {
        return refontouml_association;
    }

    public void setRefontouml_association(RefOntoUML_Association refontouml_association) {
        this.refontouml_association = refontouml_association;
    }
    public RefOntoUML_Association getRefontouml_association() {
        return refontouml_association;
    }

    public void setRefontouml_association(RefOntoUML_Association refontouml_association) {
        this.refontouml_association = refontouml_association;
    }
    public RefOntoUML_Property getRefontouml_property() {
        return refontouml_property;
    }

    public void setRefontouml_property(RefOntoUML_Property refontouml_property) {
        this.refontouml_property = refontouml_property;
    }
    public List<RefOntoUML_Property> getRefontouml_propertys() {
        return refontouml_propertys;
    }

    public void addRefontouml_property(Refontouml_property refontouml_property) {
        this.refontouml_propertys.add(refontouml_property);
    }
    public RefOntoUML_Class getRefontouml_class() {
        return refontouml_class;
    }

    public void setRefontouml_class(RefOntoUML_Class refontouml_class) {
        this.refontouml_class = refontouml_class;
    }
    public RefOntoUML_Association getRefontouml_association() {
        return refontouml_association;
    }

    public void setRefontouml_association(RefOntoUML_Association refontouml_association) {
        this.refontouml_association = refontouml_association;
    }
    public RefOntoUML_Association getRefontouml_association() {
        return refontouml_association;
    }

    public void setRefontouml_association(RefOntoUML_Association refontouml_association) {
        this.refontouml_association = refontouml_association;
    }
    public RefOntoUML_DataType getRefontouml_datatype() {
        return refontouml_datatype;
    }

    public void setRefontouml_datatype(RefOntoUML_DataType refontouml_datatype) {
        this.refontouml_datatype = refontouml_datatype;
    }
    public RefOntoUML_Classifier getRefontouml_classifier() {
        return refontouml_classifier;
    }

    public void setRefontouml_classifier(RefOntoUML_Classifier refontouml_classifier) {
        this.refontouml_classifier = refontouml_classifier;
    }

}