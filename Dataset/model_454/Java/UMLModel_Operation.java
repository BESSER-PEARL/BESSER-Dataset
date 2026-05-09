





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Operation extends TemplateableElement, BehavioralFeature, ParameterableElement {

    private String postcondition;
    private String lower;
    private String interface;
    private String precondition;
    private String class_;
    private String bodyCondition;
    private String isQuery;
    private String isUnique;
    private String isOrdered;
    private String datatype;
    private String redefinedOperation;
    private String type;
    private String upper;





    private UMLModel_DataType umlmodel_datatype;


    public UMLModel_Operation(
        String postcondition,        String lower,        String interface,        String precondition,        String class_,        String bodyCondition,        String isQuery,        String isUnique,        String isOrdered,        String datatype,        String redefinedOperation,        String type,        String upper    ) {
        super(
        );
        this.postcondition = postcondition;
        this.lower = lower;
        this.interface = interface;
        this.precondition = precondition;
        this.class_ = class_;
        this.bodyCondition = bodyCondition;
        this.isQuery = isQuery;
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.datatype = datatype;
        this.redefinedOperation = redefinedOperation;
        this.type = type;
        this.upper = upper;
    }


    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getBodycondition() {
        return bodyCondition;
    }

    public void setBodycondition(String bodyCondition) {
        this.bodyCondition = bodyCondition;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getDatatype() {
        return datatype;
    }

    public void setDatatype(String datatype) {
        this.datatype = datatype;
    }
    public String getRedefinedoperation() {
        return redefinedOperation;
    }

    public void setRedefinedoperation(String redefinedOperation) {
        this.redefinedOperation = redefinedOperation;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public UMLModel_DataType getUmlmodel_datatype() {
        return umlmodel_datatype;
    }

    public void setUmlmodel_datatype(UMLModel_DataType umlmodel_datatype) {
        this.umlmodel_datatype = umlmodel_datatype;
    }

}