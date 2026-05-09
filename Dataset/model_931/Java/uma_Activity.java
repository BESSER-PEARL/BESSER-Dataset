





import java.util.List;
import java.util.ArrayList;

public class uma_Activity extends WorkBreakdownElement, WorkDefinition, VariabilityElement {

    private String isEnactable;





    private List<uma_ReusableAsset> uma_reusableassets;




    private List<uma_Example> uma_examples;


    public uma_Activity(
        String isEnactable    ) {
        super(
        );
        this.isEnactable = isEnactable;
        this.uma_reusableassets = new ArrayList<>();
        this.uma_examples = new ArrayList<>();
    }

    public uma_Activity(
        String isEnactable        ArrayList<uma_ReusableAsset> uma_reusableassets,        ArrayList<uma_Example> uma_examples    ) {
        this.isEnactable = isEnactable;
        this.uma_reusableassets = uma_reusableassets;
        this.uma_examples = uma_examples;
    }

    public String getIsenactable() {
        return isEnactable;
    }

    public void setIsenactable(String isEnactable) {
        this.isEnactable = isEnactable;
    }

    public List<uma_ReusableAsset> getUma_reusableassets() {
        return uma_reusableassets;
    }

    public void addUma_reusableasset(Uma_reusableasset uma_reusableasset) {
        this.uma_reusableassets.add(uma_reusableasset);
    }
    public List<uma_Example> getUma_examples() {
        return uma_examples;
    }

    public void addUma_example(Uma_example uma_example) {
        this.uma_examples.add(uma_example);
    }

}