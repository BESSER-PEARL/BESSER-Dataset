





import java.util.List;
import java.util.ArrayList;

public class uma_BreakdownElement extends ProcessElement {

    private String planningData;
    private String guideline;
    private String presentedBefore;
    private String example;
    private String presentedAfter;
    private String checklist;
    private String isPlanned;
    private String concept;
    private String reusableAsset;
    private String supportingMaterial;
    private String prefix;
    private String whitepaper;
    private String superActivity;
    private String isOptional;
    private String group1;
    private String hasMultipleOccurrences;





    private uma_Activity uma_activity;


    public uma_BreakdownElement(
        String planningData,        String guideline,        String presentedBefore,        String example,        String presentedAfter,        String checklist,        String isPlanned,        String concept,        String reusableAsset,        String supportingMaterial,        String prefix,        String whitepaper,        String superActivity,        String isOptional,        String group1,        String hasMultipleOccurrences    ) {
        super(
        );
        this.planningData = planningData;
        this.guideline = guideline;
        this.presentedBefore = presentedBefore;
        this.example = example;
        this.presentedAfter = presentedAfter;
        this.checklist = checklist;
        this.isPlanned = isPlanned;
        this.concept = concept;
        this.reusableAsset = reusableAsset;
        this.supportingMaterial = supportingMaterial;
        this.prefix = prefix;
        this.whitepaper = whitepaper;
        this.superActivity = superActivity;
        this.isOptional = isOptional;
        this.group1 = group1;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }


    public String getPlanningdata() {
        return planningData;
    }

    public void setPlanningdata(String planningData) {
        this.planningData = planningData;
    }
    public String getGuideline() {
        return guideline;
    }

    public void setGuideline(String guideline) {
        this.guideline = guideline;
    }
    public String getPresentedbefore() {
        return presentedBefore;
    }

    public void setPresentedbefore(String presentedBefore) {
        this.presentedBefore = presentedBefore;
    }
    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getPresentedafter() {
        return presentedAfter;
    }

    public void setPresentedafter(String presentedAfter) {
        this.presentedAfter = presentedAfter;
    }
    public String getChecklist() {
        return checklist;
    }

    public void setChecklist(String checklist) {
        this.checklist = checklist;
    }
    public String getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(String isPlanned) {
        this.isPlanned = isPlanned;
    }
    public String getConcept() {
        return concept;
    }

    public void setConcept(String concept) {
        this.concept = concept;
    }
    public String getReusableasset() {
        return reusableAsset;
    }

    public void setReusableasset(String reusableAsset) {
        this.reusableAsset = reusableAsset;
    }
    public String getSupportingmaterial() {
        return supportingMaterial;
    }

    public void setSupportingmaterial(String supportingMaterial) {
        this.supportingMaterial = supportingMaterial;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
    }
    public String getSuperactivity() {
        return superActivity;
    }

    public void setSuperactivity(String superActivity) {
        this.superActivity = superActivity;
    }
    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(String hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }

    public uma_Activity getUma_activity() {
        return uma_activity;
    }

    public void setUma_activity(uma_Activity uma_activity) {
        this.uma_activity = uma_activity;
    }

}