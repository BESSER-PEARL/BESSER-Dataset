





import java.util.List;
import java.util.ArrayList;

public class sample_Given  {






    private sample_Scenario sample_scenario;




    private List<sample_Sentence> sample_sentences;


    public sample_Given(
    ) {
        this.sample_sentences = new ArrayList<>();
    }

    public sample_Given(
        ArrayList<sample_Sentence> sample_sentences    ) {
        this.sample_sentences = sample_sentences;
    }


    public sample_Scenario getSample_scenario() {
        return sample_scenario;
    }

    public void setSample_scenario(sample_Scenario sample_scenario) {
        this.sample_scenario = sample_scenario;
    }
    public List<sample_Sentence> getSample_sentences() {
        return sample_sentences;
    }

    public void addSample_sentence(Sample_sentence sample_sentence) {
        this.sample_sentences.add(sample_sentence);
    }

}