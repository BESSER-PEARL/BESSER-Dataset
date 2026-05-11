





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcETypedElement extends SrcENamedElement {

    private int lowerBound;
    private int upperBound;
    private boolean ordered;
    private boolean many;
    private boolean required;
    private boolean unique;





    private jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier;


    public jointPackage_Ecore2Maude_SrcETypedElement(
        int lowerBound,        int upperBound,        boolean ordered,        boolean many,        boolean required,        boolean unique    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.ordered = ordered;
        this.many = many;
        this.required = required;
        this.unique = unique;
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
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
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

    public jointPackage_Ecore2Maude_SrcEClassifier getJointpackage_ecore2maude_srceclassifier() {
        return jointpackage_ecore2maude_srceclassifier;
    }

    public void setJointpackage_ecore2maude_srceclassifier(jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier) {
        this.jointpackage_ecore2maude_srceclassifier = jointpackage_ecore2maude_srceclassifier;
    }

}