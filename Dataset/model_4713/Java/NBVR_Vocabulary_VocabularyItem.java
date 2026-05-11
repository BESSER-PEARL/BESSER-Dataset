





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_VocabularyItem  {






    private List<VocabularyItem> vocabularyitems;




    private List<Term> terms;




    private VocabularyItem vocabularyitem;


    public NBVR_Vocabulary_VocabularyItem(
    ) {
        this.vocabularyitems = new ArrayList<>();
        this.terms = new ArrayList<>();
    }

    public NBVR_Vocabulary_VocabularyItem(
        ArrayList<VocabularyItem> vocabularyitems,        ArrayList<Term> terms    ) {
        this.vocabularyitems = vocabularyitems;
        this.terms = terms;
    }


    public List<VocabularyItem> getVocabularyitems() {
        return vocabularyitems;
    }

    public void addVocabularyitem(Vocabularyitem vocabularyitem) {
        this.vocabularyitems.add(vocabularyitem);
    }
    public List<Term> getTerms() {
        return terms;
    }

    public void addTerm(Term term) {
        this.terms.add(term);
    }
    public VocabularyItem getVocabularyitem() {
        return vocabularyitem;
    }

    public void setVocabularyitem(VocabularyItem vocabularyitem) {
        this.vocabularyitem = vocabularyitem;
    }

}