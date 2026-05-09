





import java.util.List;
import java.util.ArrayList;

public class uma_ContentElement extends DescribableElement {

    private String variabilityType;
    private String reusableAsset;
    private String whitepaper;
    private String example;
    private String concept;
    private String supportingMaterial;
    private String group1;
    private String checklist;
    private String guideline;
    private String variabilityBasedOnElement;





    private uma_ContentPackage uma_contentpackage;


    public uma_ContentElement(
        String variabilityType,        String reusableAsset,        String whitepaper,        String example,        String concept,        String supportingMaterial,        String group1,        String checklist,        String guideline,        String variabilityBasedOnElement    ) {
        super(
        );
        this.variabilityType = variabilityType;
        this.reusableAsset = reusableAsset;
        this.whitepaper = whitepaper;
        this.example = example;
        this.concept = concept;
        this.supportingMaterial = supportingMaterial;
        this.group1 = group1;
        this.checklist = checklist;
        this.guideline = guideline;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
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
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
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
    public String getSupportingmaterial() {
        return supportingMaterial;
    }

    public void setSupportingmaterial(String supportingMaterial) {
        this.supportingMaterial = supportingMaterial;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getChecklist() {
        return checklist;
    }

    public void setChecklist(String checklist) {
        this.checklist = checklist;
    }
    public String getGuideline() {
        return guideline;
    }

    public void setGuideline(String guideline) {
        this.guideline = guideline;
    }
    public String getVariabilitybasedonelement() {
        return variabilityBasedOnElement;
    }

    public void setVariabilitybasedonelement(String variabilityBasedOnElement) {
        this.variabilityBasedOnElement = variabilityBasedOnElement;
    }

    public uma_ContentPackage getUma_contentpackage() {
        return uma_contentpackage;
    }

    public void setUma_contentpackage(uma_ContentPackage uma_contentpackage) {
        this.uma_contentpackage = uma_contentpackage;
    }

}