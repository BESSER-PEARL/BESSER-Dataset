





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_Term  {

    private String text;





    private List<Word> words;


    public NBVR_Vocabulary_Term(
        String text    ) {
        this.text = text;
        this.words = new ArrayList<>();
    }

    public NBVR_Vocabulary_Term(
        String text        ArrayList<Word> words    ) {
        this.text = text;
        this.words = words;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public List<Word> getWords() {
        return words;
    }

    public void addWord(Word word) {
        this.words.add(word);
    }

}