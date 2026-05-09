





import java.util.List;
import java.util.ArrayList;

public class uma_ContentElement extends VariabilityElement, DescribableElement {






    private List<uma_Concept> uma_concepts;




    private List<uma_Guideline> uma_guidelines;




    private List<uma_TermDefinition> uma_termdefinitions;




    private List<uma_ReusableAsset> uma_reusableassets;




    private uma_Practice uma_practice;




    private List<uma_Checklist> uma_checklists;




    private List<uma_SupportingMaterial> uma_supportingmaterials;




    private List<uma_Example> uma_examples;


    public uma_ContentElement(
    ) {
        super(
        );
        this.uma_concepts = new ArrayList<>();
        this.uma_guidelines = new ArrayList<>();
        this.uma_termdefinitions = new ArrayList<>();
        this.uma_reusableassets = new ArrayList<>();
        this.uma_checklists = new ArrayList<>();
        this.uma_supportingmaterials = new ArrayList<>();
        this.uma_examples = new ArrayList<>();
    }

    public uma_ContentElement(
        ArrayList<uma_Concept> uma_concepts,        ArrayList<uma_Guideline> uma_guidelines,        ArrayList<uma_TermDefinition> uma_termdefinitions,        ArrayList<uma_ReusableAsset> uma_reusableassets,        ArrayList<uma_Checklist> uma_checklists,        ArrayList<uma_SupportingMaterial> uma_supportingmaterials,        ArrayList<uma_Example> uma_examples    ) {
        this.uma_concepts = uma_concepts;
        this.uma_guidelines = uma_guidelines;
        this.uma_termdefinitions = uma_termdefinitions;
        this.uma_reusableassets = uma_reusableassets;
        this.uma_checklists = uma_checklists;
        this.uma_supportingmaterials = uma_supportingmaterials;
        this.uma_examples = uma_examples;
    }


    public List<uma_Concept> getUma_concepts() {
        return uma_concepts;
    }

    public void addUma_concept(Uma_concept uma_concept) {
        this.uma_concepts.add(uma_concept);
    }
    public List<uma_Guideline> getUma_guidelines() {
        return uma_guidelines;
    }

    public void addUma_guideline(Uma_guideline uma_guideline) {
        this.uma_guidelines.add(uma_guideline);
    }
    public List<uma_TermDefinition> getUma_termdefinitions() {
        return uma_termdefinitions;
    }

    public void addUma_termdefinition(Uma_termdefinition uma_termdefinition) {
        this.uma_termdefinitions.add(uma_termdefinition);
    }
    public List<uma_ReusableAsset> getUma_reusableassets() {
        return uma_reusableassets;
    }

    public void addUma_reusableasset(Uma_reusableasset uma_reusableasset) {
        this.uma_reusableassets.add(uma_reusableasset);
    }
    public uma_Practice getUma_practice() {
        return uma_practice;
    }

    public void setUma_practice(uma_Practice uma_practice) {
        this.uma_practice = uma_practice;
    }
    public List<uma_Checklist> getUma_checklists() {
        return uma_checklists;
    }

    public void addUma_checklist(Uma_checklist uma_checklist) {
        this.uma_checklists.add(uma_checklist);
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

}