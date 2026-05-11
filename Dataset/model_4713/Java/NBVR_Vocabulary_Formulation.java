





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_Formulation  {

    private String language;
    private String text;





    private VocabularyItem vocabularyitem;




    private List<ParseElement> parseelements;


    public NBVR_Vocabulary_Formulation(
        String language,        String text    ) {
        this.language = language;
        this.text = text;
        this.parseelements = new ArrayList<>();
    }

    public NBVR_Vocabulary_Formulation(
        String language,        String text        ArrayList<ParseElement> parseelements    ) {
        this.language = language;
        this.text = text;
        this.parseelements = parseelements;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public VocabularyItem getVocabularyitem() {
        return vocabularyitem;
    }

    public void setVocabularyitem(VocabularyItem vocabularyitem) {
        this.vocabularyitem = vocabularyitem;
    }
    public List<ParseElement> getParseelements() {
        return parseelements;
    }

    public void addParseelement(Parseelement parseelement) {
        this.parseelements.add(parseelement);
    }

}