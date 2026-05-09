





import java.util.List;
import java.util.ArrayList;

public class uma_BreakdownElement extends ProcessElement {

    private String isPlanned;
    private String hasMultipleOccurrences;
    private String presentedAfter;
    private String presentedBefore;
    private String reusableAsset;
    private String supportingMaterial;
    private String example;
    private String isOptional;
    private String superActivity;
    private String prefix;
    private String planningData;
    private String group1;
    private String concept;
    private String guideline;
    private String checklist;
    private String whitepaper;



    public uma_BreakdownElement(
        String isPlanned,        String hasMultipleOccurrences,        String presentedAfter,        String presentedBefore,        String reusableAsset,        String supportingMaterial,        String example,        String isOptional,        String superActivity,        String prefix,        String planningData,        String group1,        String concept,        String guideline,        String checklist,        String whitepaper    ) {
        super(
        );
        this.isPlanned = isPlanned;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.presentedAfter = presentedAfter;
        this.presentedBefore = presentedBefore;
        this.reusableAsset = reusableAsset;
        this.supportingMaterial = supportingMaterial;
        this.example = example;
        this.isOptional = isOptional;
        this.superActivity = superActivity;
        this.prefix = prefix;
        this.planningData = planningData;
        this.group1 = group1;
        this.concept = concept;
        this.guideline = guideline;
        this.checklist = checklist;
        this.whitepaper = whitepaper;
    }


    public String getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(String isPlanned) {
        this.isPlanned = isPlanned;
    }
    public String getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(String hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }
    public String getPresentedafter() {
        return presentedAfter;
    }

    public void setPresentedafter(String presentedAfter) {
        this.presentedAfter = presentedAfter;
    }
    public String getPresentedbefore() {
        return presentedBefore;
    }

    public void setPresentedbefore(String presentedBefore) {
        this.presentedBefore = presentedBefore;
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
    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }
    public String getSuperactivity() {
        return superActivity;
    }

    public void setSuperactivity(String superActivity) {
        this.superActivity = superActivity;
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
    public String getGuideline() {
        return guideline;
    }

    public void setGuideline(String guideline) {
        this.guideline = guideline;
    }
    public String getChecklist() {
        return checklist;
    }

    public void setChecklist(String checklist) {
        this.checklist = checklist;
    }
    public String getWhitepaper() {
        return whitepaper;
    }

    public void setWhitepaper(String whitepaper) {
        this.whitepaper = whitepaper;
    }


}