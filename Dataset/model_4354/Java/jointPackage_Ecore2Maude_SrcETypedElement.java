





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcETypedElement extends SrcENamedElement {

    private boolean many;
    private boolean required;
    private boolean ordered;
    private int upperBound;
    private boolean unique;
    private int lowerBound;





    private jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier;


    public jointPackage_Ecore2Maude_SrcETypedElement(
        boolean many,        boolean required,        boolean ordered,        int upperBound,        boolean unique,        int lowerBound    ) {
        super(
        );
        this.many = many;
        this.required = required;
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.unique = unique;
        this.lowerBound = lowerBound;
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
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public jointPackage_Ecore2Maude_SrcEClassifier getJointpackage_ecore2maude_srceclassifier() {
        return jointpackage_ecore2maude_srceclassifier;
    }

    public void setJointpackage_ecore2maude_srceclassifier(jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier) {
        this.jointpackage_ecore2maude_srceclassifier = jointpackage_ecore2maude_srceclassifier;
    }

}