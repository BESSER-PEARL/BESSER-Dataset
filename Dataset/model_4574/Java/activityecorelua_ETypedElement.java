





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_ETypedElement extends ENamedElement {

    private boolean many;
    private boolean required;
    private boolean unique;
    private boolean ordered;
    private int lowerBound;
    private int upperBound;





    private activityecorelua_EClassifier activityecorelua_eclassifier;




    private activityecorelua_EGenericType activityecorelua_egenerictype;


    public activityecorelua_ETypedElement(
        boolean many,        boolean required,        boolean unique,        boolean ordered,        int lowerBound,        int upperBound    ) {
        super(
        );
        this.many = many;
        this.required = required;
        this.unique = unique;
        this.ordered = ordered;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public activityecorelua_EClassifier getActivityecorelua_eclassifier() {
        return activityecorelua_eclassifier;
    }

    public void setActivityecorelua_eclassifier(activityecorelua_EClassifier activityecorelua_eclassifier) {
        this.activityecorelua_eclassifier = activityecorelua_eclassifier;
    }
    public activityecorelua_EGenericType getActivityecorelua_egenerictype() {
        return activityecorelua_egenerictype;
    }

    public void setActivityecorelua_egenerictype(activityecorelua_EGenericType activityecorelua_egenerictype) {
        this.activityecorelua_egenerictype = activityecorelua_egenerictype;
    }

}