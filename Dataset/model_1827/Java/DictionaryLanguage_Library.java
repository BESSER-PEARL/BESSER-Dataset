





import java.util.List;
import java.util.ArrayList;

public class DictionaryLanguage_Library  {

    private String name;





    private List<DictionaryLanguage_Author> dictionarylanguage_authors;




    private DictionaryLanguage_Author dictionarylanguage_author;


    public DictionaryLanguage_Library(
        String name    ) {
        this.name = name;
        this.dictionarylanguage_authors = new ArrayList<>();
    }

    public DictionaryLanguage_Library(
        String name        ArrayList<DictionaryLanguage_Author> dictionarylanguage_authors    ) {
        this.name = name;
        this.dictionarylanguage_authors = dictionarylanguage_authors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<DictionaryLanguage_Author> getDictionarylanguage_authors() {
        return dictionarylanguage_authors;
    }

    public void addDictionarylanguage_author(Dictionarylanguage_author dictionarylanguage_author) {
        this.dictionarylanguage_authors.add(dictionarylanguage_author);
    }
    public DictionaryLanguage_Author getDictionarylanguage_author() {
        return dictionarylanguage_author;
    }

    public void setDictionarylanguage_author(DictionaryLanguage_Author dictionarylanguage_author) {
        this.dictionarylanguage_author = dictionarylanguage_author;
    }

}