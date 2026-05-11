





import java.util.List;
import java.util.ArrayList;

public class tortugaDSL_CONTROL_SENTENCES extends SENTENCE {






    private List<tortugaDSL_SENTENCE> tortugadsl_sentences;


    public tortugaDSL_CONTROL_SENTENCES(
    ) {
        super(
        );
        this.tortugadsl_sentences = new ArrayList<>();
    }

    public tortugaDSL_CONTROL_SENTENCES(
        ArrayList<tortugaDSL_SENTENCE> tortugadsl_sentences    ) {
        this.tortugadsl_sentences = tortugadsl_sentences;
    }


    public List<tortugaDSL_SENTENCE> getTortugadsl_sentences() {
        return tortugadsl_sentences;
    }

    public void addTortugadsl_sentence(Tortugadsl_sentence tortugadsl_sentence) {
        this.tortugadsl_sentences.add(tortugadsl_sentence);
    }

}