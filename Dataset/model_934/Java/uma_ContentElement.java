





import java.util.List;
import java.util.ArrayList;

public class uma_ContentElement extends DescribableElement {

    private String variabilityBasedOnElement;
    private String variabilityType;
    private String whitepaper;
    private String group1;
    private String concept;
    private String checklist;
    private String supportingMaterial;
    private String example;
    private String reusableAsset;
    private String guideline;





    private uma_ContentPackage uma_contentpackage;


    public uma_ContentElement(
        String variabilityBasedOnElement,        String variabilityType,        String whitepaper,        String group1,        String concept,        String checklist,        String supportingMaterial,        String example,        String reusableAsset,        String guideline    ) {
        super(
        );
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.variabilityType = variabilityType;
        this.whitepaper = whitepaper;
        this.group1 = group1;
        this.concept = concept;
        this.checklist = checklist;
        this.supportingMaterial = supportingMaterial;
        this.example = example;
        this.reusableAsset = reusableAsset;
        this.guideline = guideline;
    }


    public String getVariabilitybasedonelement() {
        return variabilityBasedOnElement;
    }

    public void setVariabilitybasedonelement(String variabilityBasedOnElement) {
        this.variabilityBasedOnElement = variabilityBasedOnElement;
    }
    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getConcept() {
        return concept;
    }

    public void setConcept(String concept) {
        this.concept = concept;
    }
    public String getChecklist() {
        return checklist;
    }

    public void setChecklist(String checklist) {
        this.checklist = checklist;
    }
    public String getSupportingmaterial() {
        return supportingMaterial;
    }

    public void setSupportingmaterial(String supportingMaterial) {
        this.supportingMaterial = supportingMaterial;
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
    public String getGuideline() {
        return guideline;
    }

    public void setGuideline(String guideline) {
        this.guideline = guideline;
    }

    public uma_ContentPackage getUma_contentpackage() {
        return uma_contentpackage;
    }

    public void setUma_contentpackage(uma_ContentPackage uma_contentpackage) {
        this.uma_contentpackage = uma_contentpackage;
    }

}