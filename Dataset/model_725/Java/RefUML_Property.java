





import java.util.List;
import java.util.ArrayList;

public class RefUML_Property extends StructuralFeature {

    private String isComposite;
    private String isDerivedUnion;
    private String aggregation;
    private String isDerived;
    private String default;





    private RefUML_Association refuml_association;




    private RefUML_Property refuml_property;




    private RefUML_Class refuml_class;




    private RefUML_DataType refuml_datatype;




    private RefUML_Association refuml_association;




    private RefUML_ValueSpecification refuml_valuespecification;




    private RefUML_Class refuml_class;




    private RefUML_DataType refuml_datatype;




    private RefUML_Classifier refuml_classifier;




    private List<RefUML_Property> refuml_propertys;




    private RefUML_Association refuml_association;




    private RefUML_Association refuml_association;




    private List<RefUML_Property> refuml_propertys;




    private RefUML_Association refuml_association;


    public RefUML_Property(
        String isComposite,        String isDerivedUnion,        String aggregation,        String isDerived,        String default    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.isDerived = isDerived;
        this.default = default;
        this.refuml_propertys = new ArrayList<>();
        this.refuml_propertys = new ArrayList<>();
    }

    public RefUML_Property(
        String isComposite,        String isDerivedUnion,        String aggregation,        String isDerived,        String default        ArrayList<RefUML_Property> refuml_propertys,        ArrayList<RefUML_Property> refuml_propertys    ) {
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.aggregation = aggregation;
        this.isDerived = isDerived;
        this.default = default;
        this.refuml_propertys = refuml_propertys;
        this.refuml_propertys = refuml_propertys;
    }

    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
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
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public RefUML_Association getRefuml_association() {
        return refuml_association;
    }

    public void setRefuml_association(RefUML_Association refuml_association) {
        this.refuml_association = refuml_association;
    }
    public RefUML_Property getRefuml_property() {
        return refuml_property;
    }

    public void setRefuml_property(RefUML_Property refuml_property) {
        this.refuml_property = refuml_property;
    }
    public RefUML_Class getRefuml_class() {
        return refuml_class;
    }

    public void setRefuml_class(RefUML_Class refuml_class) {
        this.refuml_class = refuml_class;
    }
    public RefUML_DataType getRefuml_datatype() {
        return refuml_datatype;
    }

    public void setRefuml_datatype(RefUML_DataType refuml_datatype) {
        this.refuml_datatype = refuml_datatype;
    }
    public RefUML_Association getRefuml_association() {
        return refuml_association;
    }

    public void setRefuml_association(RefUML_Association refuml_association) {
        this.refuml_association = refuml_association;
    }
    public RefUML_ValueSpecification getRefuml_valuespecification() {
        return refuml_valuespecification;
    }

    public void setRefuml_valuespecification(RefUML_ValueSpecification refuml_valuespecification) {
        this.refuml_valuespecification = refuml_valuespecification;
    }
    public RefUML_Class getRefuml_class() {
        return refuml_class;
    }

    public void setRefuml_class(RefUML_Class refuml_class) {
        this.refuml_class = refuml_class;
    }
    public RefUML_DataType getRefuml_datatype() {
        return refuml_datatype;
    }

    public void setRefuml_datatype(RefUML_DataType refuml_datatype) {
        this.refuml_datatype = refuml_datatype;
    }
    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }
    public List<RefUML_Property> getRefuml_propertys() {
        return refuml_propertys;
    }

    public void addRefuml_property(Refuml_property refuml_property) {
        this.refuml_propertys.add(refuml_property);
    }
    public RefUML_Association getRefuml_association() {
        return refuml_association;
    }

    public void setRefuml_association(RefUML_Association refuml_association) {
        this.refuml_association = refuml_association;
    }
    public RefUML_Association getRefuml_association() {
        return refuml_association;
    }

    public void setRefuml_association(RefUML_Association refuml_association) {
        this.refuml_association = refuml_association;
    }
    public List<RefUML_Property> getRefuml_propertys() {
        return refuml_propertys;
    }

    public void addRefuml_property(Refuml_property refuml_property) {
        this.refuml_propertys.add(refuml_property);
    }
    public RefUML_Association getRefuml_association() {
        return refuml_association;
    }

    public void setRefuml_association(RefUML_Association refuml_association) {
        this.refuml_association = refuml_association;
    }

}