





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private String required;
    private String many;
    private String lowerBound;
    private String unique;
    private String ordered;
    private String upperBound;





    private EGenericType egenerictype;




    private EClassifier eclassifier;


    public ecore_ETypedElement(
        String required,        String many,        String lowerBound,        String unique,        String ordered,        String upperBound    ) {
        super(
        );
        this.required = required;
        this.many = many;
        this.lowerBound = lowerBound;
        this.unique = unique;
        this.ordered = ordered;
        this.upperBound = upperBound;
    }


    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getUnique() {
        return unique;
    }

    public void setUnique(String unique) {
        this.unique = unique;
    }
    public String getOrdered() {
        return ordered;
    }

    public void setOrdered(String ordered) {
        this.ordered = ordered;
    }
    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }

    public EGenericType getEgenerictype() {
        return egenerictype;
    }

    public void setEgenerictype(EGenericType egenerictype) {
        this.egenerictype = egenerictype;
    }
    public EClassifier getEclassifier() {
        return eclassifier;
    }

    public void setEclassifier(EClassifier eclassifier) {
        this.eclassifier = eclassifier;
    }

}