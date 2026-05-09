





import java.util.List;
import java.util.ArrayList;

public class uma_ContentElement extends VariabilityElement, DescribableElement {






    private List<uma_Example> uma_examples;




    private List<uma_ReusableAsset> uma_reusableassets;




    private List<uma_TermDefinition> uma_termdefinitions;


    public uma_ContentElement(
    ) {
        super(
        );
        this.uma_examples = new ArrayList<>();
        this.uma_reusableassets = new ArrayList<>();
        this.uma_termdefinitions = new ArrayList<>();
    }

    public uma_ContentElement(
        ArrayList<uma_Example> uma_examples,        ArrayList<uma_ReusableAsset> uma_reusableassets,        ArrayList<uma_TermDefinition> uma_termdefinitions    ) {
        this.uma_examples = uma_examples;
        this.uma_reusableassets = uma_reusableassets;
        this.uma_termdefinitions = uma_termdefinitions;
    }


    public List<uma_Example> getUma_examples() {
        return uma_examples;
    }

    public void addUma_example(Uma_example uma_example) {
        this.uma_examples.add(uma_example);
    }
    public List<uma_ReusableAsset> getUma_reusableassets() {
        return uma_reusableassets;
    }

    public void addUma_reusableasset(Uma_reusableasset uma_reusableasset) {
        this.uma_reusableassets.add(uma_reusableasset);
    }
    public List<uma_TermDefinition> getUma_termdefinitions() {
        return uma_termdefinitions;
    }

    public void addUma_termdefinition(Uma_termdefinition uma_termdefinition) {
        this.uma_termdefinitions.add(uma_termdefinition);
    }

}