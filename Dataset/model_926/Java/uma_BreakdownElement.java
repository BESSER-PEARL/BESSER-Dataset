





import java.util.List;
import java.util.ArrayList;

public class uma_BreakdownElement extends ProcessElement {

    private String isOptional;
    private String isPlanned;
    private String prefix;
    private String hasMultipleOccurrences;





    private List<uma_Guideline> uma_guidelines;




    private List<uma_Report> uma_reports;




    private uma_BreakdownElement uma_breakdownelement;




    private List<uma_ToolMentor> uma_toolmentors;




    private uma_BreakdownElement uma_breakdownelement;




    private List<uma_SupportingMaterial> uma_supportingmaterials;




    private List<uma_Example> uma_examples;




    private List<uma_Checklist> uma_checklists;




    private uma_Activity uma_activity;




    private List<uma_Concept> uma_concepts;




    private List<uma_EstimationConsiderations> uma_estimationconsiderationss;




    private List<uma_ReusableAsset> uma_reusableassets;




    private uma_Activity uma_activity;




    private uma_PlanningData uma_planningdata;




    private List<uma_Template> uma_templates;


    public uma_BreakdownElement(
        String isOptional,        String isPlanned,        String prefix,        String hasMultipleOccurrences    ) {
        super(
        );
        this.isOptional = isOptional;
        this.isPlanned = isPlanned;
        this.prefix = prefix;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.uma_guidelines = new ArrayList<>();
        this.uma_reports = new ArrayList<>();
        this.uma_toolmentors = new ArrayList<>();
        this.uma_supportingmaterials = new ArrayList<>();
        this.uma_examples = new ArrayList<>();
        this.uma_checklists = new ArrayList<>();
        this.uma_concepts = new ArrayList<>();
        this.uma_estimationconsiderationss = new ArrayList<>();
        this.uma_reusableassets = new ArrayList<>();
        this.uma_templates = new ArrayList<>();
    }

    public uma_BreakdownElement(
        String isOptional,        String isPlanned,        String prefix,        String hasMultipleOccurrences        ArrayList<uma_Guideline> uma_guidelines,        ArrayList<uma_Report> uma_reports,        ArrayList<uma_ToolMentor> uma_toolmentors,        ArrayList<uma_SupportingMaterial> uma_supportingmaterials,        ArrayList<uma_Example> uma_examples,        ArrayList<uma_Checklist> uma_checklists,        ArrayList<uma_Concept> uma_concepts,        ArrayList<uma_EstimationConsiderations> uma_estimationconsiderationss,        ArrayList<uma_ReusableAsset> uma_reusableassets,        ArrayList<uma_Template> uma_templates    ) {
        this.isOptional = isOptional;
        this.isPlanned = isPlanned;
        this.prefix = prefix;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.uma_guidelines = uma_guidelines;
        this.uma_reports = uma_reports;
        this.uma_toolmentors = uma_toolmentors;
        this.uma_supportingmaterials = uma_supportingmaterials;
        this.uma_examples = uma_examples;
        this.uma_checklists = uma_checklists;
        this.uma_concepts = uma_concepts;
        this.uma_estimationconsiderationss = uma_estimationconsiderationss;
        this.uma_reusableassets = uma_reusableassets;
        this.uma_templates = uma_templates;
    }

    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }
    public String getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(String isPlanned) {
        this.isPlanned = isPlanned;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(String hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }

    public List<uma_Guideline> getUma_guidelines() {
        return uma_guidelines;
    }

    public void addUma_guideline(Uma_guideline uma_guideline) {
        this.uma_guidelines.add(uma_guideline);
    }
    public List<uma_Report> getUma_reports() {
        return uma_reports;
    }

    public void addUma_report(Uma_report uma_report) {
        this.uma_reports.add(uma_report);
    }
    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }
    public List<uma_ToolMentor> getUma_toolmentors() {
        return uma_toolmentors;
    }

    public void addUma_toolmentor(Uma_toolmentor uma_toolmentor) {
        this.uma_toolmentors.add(uma_toolmentor);
    }
    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }
    public List<uma_SupportingMaterial> getUma_supportingmaterials() {
        return uma_supportingmaterials;
    }

    public void addUma_supportingmaterial(Uma_supportingmaterial uma_supportingmaterial) {
        this.uma_supportingmaterials.add(uma_supportingmaterial);
    }
    public List<uma_Example> getUma_examples() {
        return uma_examples;
    }

    public void addUma_example(Uma_example uma_example) {
        this.uma_examples.add(uma_example);
    }
    public List<uma_Checklist> getUma_checklists() {
        return uma_checklists;
    }

    public void addUma_checklist(Uma_checklist uma_checklist) {
        this.uma_checklists.add(uma_checklist);
    }
    public uma_Activity getUma_activity() {
        return uma_activity;
    }

    public void setUma_activity(uma_Activity uma_activity) {
        this.uma_activity = uma_activity;
    }
    public List<uma_Concept> getUma_concepts() {
        return uma_concepts;
    }

    public void addUma_concept(Uma_concept uma_concept) {
        this.uma_concepts.add(uma_concept);
    }
    public List<uma_EstimationConsiderations> getUma_estimationconsiderationss() {
        return uma_estimationconsiderationss;
    }

    public void addUma_estimationconsiderations(Uma_estimationconsiderations uma_estimationconsiderations) {
        this.uma_estimationconsiderationss.add(uma_estimationconsiderations);
    }
    public List<uma_ReusableAsset> getUma_reusableassets() {
        return uma_reusableassets;
    }

    public void addUma_reusableasset(Uma_reusableasset uma_reusableasset) {
        this.uma_reusableassets.add(uma_reusableasset);
    }
    public uma_Activity getUma_activity() {
        return uma_activity;
    }

    public void setUma_activity(uma_Activity uma_activity) {
        this.uma_activity = uma_activity;
    }
    public uma_PlanningData getUma_planningdata() {
        return uma_planningdata;
    }

    public void setUma_planningdata(uma_PlanningData uma_planningdata) {
        this.uma_planningdata = uma_planningdata;
    }
    public List<uma_Template> getUma_templates() {
        return uma_templates;
    }

    public void addUma_template(Uma_template uma_template) {
        this.uma_templates.add(uma_template);
    }

}