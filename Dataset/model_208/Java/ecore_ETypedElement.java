





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private String lowerBound;
    private String many;
    private String unique;
    private String required;
    private String upperBound;
    private String ordered;





    private EClassifier eclassifier;




    private EGenericType egenerictype;


    public ecore_ETypedElement(
        String lowerBound,        String many,        String unique,        String required,        String upperBound,        String ordered    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.many = many;
        this.unique = unique;
        this.required = required;
        this.upperBound = upperBound;
        this.ordered = ordered;
    }


    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getUnique() {
        return unique;
    }

    public void setUnique(String unique) {
        this.unique = unique;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }
    public String getOrdered() {
        return ordered;
    }

    public void setOrdered(String ordered) {
        this.ordered = ordered;
    }

    public EClassifier getEclassifier() {
        return eclassifier;
    }

    public void setEclassifier(EClassifier eclassifier) {
        this.eclassifier = eclassifier;
    }
    public EGenericType getEgenerictype() {
        return egenerictype;
    }

    public void setEgenerictype(EGenericType egenerictype) {
        this.egenerictype = egenerictype;
    }

}