





import java.util.List;
import java.util.ArrayList;

public class uma_BreakdownElement extends ProcessElement {

    private String isOptional;
    private String whitepaper;
    private String supportingMaterial;
    private String example;
    private String presentedBefore;
    private String guideline;
    private String prefix;
    private String group1;
    private String checklist;
    private String concept;
    private String hasMultipleOccurrences;
    private String isPlanned;
    private String reusableAsset;
    private String superActivity;
    private String presentedAfter;
    private String planningData;



    public uma_BreakdownElement(
        String isOptional,        String whitepaper,        String supportingMaterial,        String example,        String presentedBefore,        String guideline,        String prefix,        String group1,        String checklist,        String concept,        String hasMultipleOccurrences,        String isPlanned,        String reusableAsset,        String superActivity,        String presentedAfter,        String planningData    ) {
        super(
        );
        this.isOptional = isOptional;
        this.whitepaper = whitepaper;
        this.supportingMaterial = supportingMaterial;
        this.example = example;
        this.presentedBefore = presentedBefore;
        this.guideline = guideline;
        this.prefix = prefix;
        this.group1 = group1;
        this.checklist = checklist;
        this.concept = concept;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.isPlanned = isPlanned;
        this.reusableAsset = reusableAsset;
        this.superActivity = superActivity;
        this.presentedAfter = presentedAfter;
        this.planningData = planningData;
    }


    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
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
    public String getPresentedbefore() {
        return presentedBefore;
    }

    public void setPresentedbefore(String presentedBefore) {
        this.presentedBefore = presentedBefore;
    }
    public String getGuideline() {
        return guideline;
    }

    public void setGuideline(String guideline) {
        this.guideline = guideline;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
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
    public String getConcept() {
        return concept;
    }

    public void setConcept(String concept) {
        this.concept = concept;
    }
    public String getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(String hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }
    public String getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(String isPlanned) {
        this.isPlanned = isPlanned;
    }
    public String getReusableasset() {
        return reusableAsset;
    }

    public void setReusableasset(String reusableAsset) {
        this.reusableAsset = reusableAsset;
    }
    public String getSuperactivity() {
        return superActivity;
    }

    public void setSuperactivity(String superActivity) {
        this.superActivity = superActivity;
    }
    public String getPresentedafter() {
        return presentedAfter;
    }

    public void setPresentedafter(String presentedAfter) {
        this.presentedAfter = presentedAfter;
    }
    public String getPlanningdata() {
        return planningData;
    }

    public void setPlanningdata(String planningData) {
        this.planningData = planningData;
    }


}