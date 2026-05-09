





import java.util.List;
import java.util.ArrayList;

public class uma_ContentElement extends DescribableElement {

    private String variabilityBasedOnElement;
    private String group1;
    private String supportingMaterial;
    private String variabilityType;
    private String reusableAsset;
    private String example;
    private String concept;
    private String guideline;
    private String whitepaper;
    private String checklist;





    private uma_ContentPackage uma_contentpackage;


    public uma_ContentElement(
        String variabilityBasedOnElement,        String group1,        String supportingMaterial,        String variabilityType,        String reusableAsset,        String example,        String concept,        String guideline,        String whitepaper,        String checklist    ) {
        super(
        );
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.group1 = group1;
        this.supportingMaterial = supportingMaterial;
        this.variabilityType = variabilityType;
        this.reusableAsset = reusableAsset;
        this.example = example;
        this.concept = concept;
        this.guideline = guideline;
        this.whitepaper = whitepaper;
        this.checklist = checklist;
    }


    public String getVariabilitybasedonelement() {
        return variabilityBasedOnElement;
    }

    public void setVariabilitybasedonelement(String variabilityBasedOnElement) {
        this.variabilityBasedOnElement = variabilityBasedOnElement;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getSupportingmaterial() {
        return supportingMaterial;
    }

    public void setSupportingmaterial(String supportingMaterial) {
        this.supportingMaterial = supportingMaterial;
    }
    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }
    public String getReusableasset() {
        return reusableAsset;
    }

    public void setReusableasset(String reusableAsset) {
        this.reusableAsset = reusableAsset;
    }
    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getConcept() {
        return concept;
    }

    public void setConcept(String concept) {
        this.concept = concept;
    }
    public String getGuideline() {
        return guideline;
    }

    public void setGuideline(String guideline) {
        this.guideline = guideline;
    }
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
    }
    public String getChecklist() {
        return checklist;
    }

    public void setChecklist(String checklist) {
        this.checklist = checklist;
    }

    public uma_ContentPackage getUma_contentpackage() {
        return uma_contentpackage;
    }

    public void setUma_contentpackage(uma_ContentPackage uma_contentpackage) {
        this.uma_contentpackage = uma_contentpackage;
    }

}