





import java.util.List;
import java.util.ArrayList;

public class uma_BreakdownElement extends ProcessElement {

    private String example;
    private String superActivity;
    private String reusableAsset;
    private String group1;
    private String prefix;
    private String planningData;
    private String concept;
    private String isOptional;
    private String hasMultipleOccurrences;
    private String presentedBefore;
    private String checklist;
    private String guideline;
    private String whitepaper;
    private String isPlanned;
    private String supportingMaterial;
    private String presentedAfter;



    public uma_BreakdownElement(
        String example,        String superActivity,        String reusableAsset,        String group1,        String prefix,        String planningData,        String concept,        String isOptional,        String hasMultipleOccurrences,        String presentedBefore,        String checklist,        String guideline,        String whitepaper,        String isPlanned,        String supportingMaterial,        String presentedAfter    ) {
        super(
        );
        this.example = example;
        this.superActivity = superActivity;
        this.reusableAsset = reusableAsset;
        this.group1 = group1;
        this.prefix = prefix;
        this.planningData = planningData;
        this.concept = concept;
        this.isOptional = isOptional;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.presentedBefore = presentedBefore;
        this.checklist = checklist;
        this.guideline = guideline;
        this.whitepaper = whitepaper;
        this.isPlanned = isPlanned;
        this.supportingMaterial = supportingMaterial;
        this.presentedAfter = presentedAfter;
    }


    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getSuperactivity() {
        return superActivity;
    }

    public void setSuperactivity(String superActivity) {
        this.superActivity = superActivity;
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
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getPlanningdata() {
        return planningData;
    }

    public void setPlanningdata(String planningData) {
        this.planningData = planningData;
    }
    public String getConcept() {
        return concept;
    }

    public void setConcept(String concept) {
        this.concept = concept;
    }
    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }
    public String getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(String hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }
    public String getPresentedbefore() {
        return presentedBefore;
    }

    public void setPresentedbefore(String presentedBefore) {
        this.presentedBefore = presentedBefore;
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
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
    }
    public String getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(String isPlanned) {
        this.isPlanned = isPlanned;
    }
    public String getSupportingmaterial() {
        return supportingMaterial;
    }

    public void setSupportingmaterial(String supportingMaterial) {
        this.supportingMaterial = supportingMaterial;
    }
    public String getPresentedafter() {
        return presentedAfter;
    }

    public void setPresentedafter(String presentedAfter) {
        this.presentedAfter = presentedAfter;
    }


}