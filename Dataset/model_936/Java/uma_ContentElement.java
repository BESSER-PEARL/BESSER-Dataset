





import java.util.List;
import java.util.ArrayList;

public class uma_ContentElement extends DescribableElement {

    private String supportingMaterial;
    private String variabilityBasedOnElement;
    private String whitepaper;
    private String concept;
    private String example;
    private String reusableAsset;
    private String group1;
    private String guideline;
    private String variabilityType;
    private String checklist;





    private uma_ContentPackage uma_contentpackage;


    public uma_ContentElement(
        String supportingMaterial,        String variabilityBasedOnElement,        String whitepaper,        String concept,        String example,        String reusableAsset,        String group1,        String guideline,        String variabilityType,        String checklist    ) {
        super(
        );
        this.supportingMaterial = supportingMaterial;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.whitepaper = whitepaper;
        this.concept = concept;
        this.example = example;
        this.reusableAsset = reusableAsset;
        this.group1 = group1;
        this.guideline = guideline;
        this.variabilityType = variabilityType;
        this.checklist = checklist;
    }


    public String getSupportingmaterial() {
        return supportingMaterial;
    }

    public void setSupportingmaterial(String supportingMaterial) {
        this.supportingMaterial = supportingMaterial;
    }
    public String getVariabilitybasedonelement() {
        return variabilityBasedOnElement;
    }

    public void setVariabilitybasedonelement(String variabilityBasedOnElement) {
        this.variabilityBasedOnElement = variabilityBasedOnElement;
    }
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
    }
    public String getConcept() {
        return concept;
    }

    public void setConcept(String concept) {
        this.concept = concept;
    }
    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getReusableasset() {
        return reusableAsset;
    }

    public void setReusableasset(String reusableAsset) {
        this.reusableAsset = reusableAsset;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getGuideline() {
        return guideline;
    }

    public void setGuideline(String guideline) {
        this.guideline = guideline;
    }
    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
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