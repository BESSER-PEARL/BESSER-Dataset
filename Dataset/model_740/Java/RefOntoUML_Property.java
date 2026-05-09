





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Property extends StructuralFeature {

    private String aggregation;
    private String isDerivedUnion;
    private String isComposite;
    private String isDerived;
    private String default;





    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_ValueSpecification refontouml_valuespecification;




    private RefOntoUML_Classifier refontouml_classifier;




    private List<RefOntoUML_Property> refontouml_propertys;




    private RefOntoUML_Association refontouml_association;




    private RefOntoUML_Property refontouml_property;




    private List<RefOntoUML_Property> refontouml_propertys;




    private RefOntoUML_Association refontouml_association;


    public RefOntoUML_Property(
        String aggregation,        String isDerivedUnion,        String isComposite,        String isDerived,        String default    ) {
        super(
        );
        this.aggregation = aggregation;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.default = default;
        this.refontouml_propertys = new ArrayList<>();
        this.refontouml_propertys = new ArrayList<>();
    }

    public RefOntoUML_Property(
        String aggregation,        String isDerivedUnion,        String isComposite,        String isDerived,        String default        ArrayList<RefOntoUML_Property> refontouml_propertys,        ArrayList<RefOntoUML_Property> refontouml_propertys    ) {
        this.aggregation = aggregation;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.default = default;
        this.refontouml_propertys = refontouml_propertys;
        this.refontouml_propertys = refontouml_propertys;
    }

    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public String getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(String isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
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
    public RefOntoUML_Association getRefontouml_association() {
        return refontouml_association;
    }

    public void setRefontouml_association(RefOntoUML_Association refontouml_association) {
        this.refontouml_association = refontouml_association;
    }
    public RefOntoUML_ValueSpecification getRefontouml_valuespecification() {
        return refontouml_valuespecification;
    }

    public void setRefontouml_valuespecification(RefOntoUML_ValueSpecification refontouml_valuespecification) {
        this.refontouml_valuespecification = refontouml_valuespecification;
    }
    public RefOntoUML_Classifier getRefontouml_classifier() {
        return refontouml_classifier;
    }

    public void setRefontouml_classifier(RefOntoUML_Classifier refontouml_classifier) {
        this.refontouml_classifier = refontouml_classifier;
    }
    public List<RefOntoUML_Property> getRefontouml_propertys() {
        return refontouml_propertys;
    }

    public void addRefontouml_property(Refontouml_property refontouml_property) {
        this.refontouml_propertys.add(refontouml_property);
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
    public RefOntoUML_Association getRefontouml_association() {
        return refontouml_association;
    }

    public void setRefontouml_association(RefOntoUML_Association refontouml_association) {
        this.refontouml_association = refontouml_association;
    }

}