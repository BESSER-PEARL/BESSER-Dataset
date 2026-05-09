





import java.util.List;
import java.util.ArrayList;

public class DictionaryLanguage_Dictionary  {

    private String title;





    private DictionaryLanguage_Author dictionarylanguage_author;




    private DictionaryLanguage_Shelf dictionarylanguage_shelf;




    private List<DictionaryLanguage_Entry> dictionarylanguage_entrys;




    private DictionaryLanguage_Author dictionarylanguage_author;




    private DictionaryLanguage_Shelf dictionarylanguage_shelf;


    public DictionaryLanguage_Dictionary(
        String title    ) {
        this.title = title;
        this.dictionarylanguage_entrys = new ArrayList<>();
    }

    public DictionaryLanguage_Dictionary(
        String title        ArrayList<DictionaryLanguage_Entry> dictionarylanguage_entrys    ) {
        this.title = title;
        this.dictionarylanguage_entrys = dictionarylanguage_entrys;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public DictionaryLanguage_Author getDictionarylanguage_author() {
        return dictionarylanguage_author;
    }

    public void setDictionarylanguage_author(DictionaryLanguage_Author dictionarylanguage_author) {
        this.dictionarylanguage_author = dictionarylanguage_author;
    }
    public DictionaryLanguage_Shelf getDictionarylanguage_shelf() {
        return dictionarylanguage_shelf;
    }

    public void setDictionarylanguage_shelf(DictionaryLanguage_Shelf dictionarylanguage_shelf) {
        this.dictionarylanguage_shelf = dictionarylanguage_shelf;
    }
    public List<DictionaryLanguage_Entry> getDictionarylanguage_entrys() {
        return dictionarylanguage_entrys;
    }

    public void addDictionarylanguage_entry(Dictionarylanguage_entry dictionarylanguage_entry) {
        this.dictionarylanguage_entrys.add(dictionarylanguage_entry);
    }
    public DictionaryLanguage_Author getDictionarylanguage_author() {
        return dictionarylanguage_author;
    }

    public void setDictionarylanguage_author(DictionaryLanguage_Author dictionarylanguage_author) {
        this.dictionarylanguage_author = dictionarylanguage_author;
    }
    public DictionaryLanguage_Shelf getDictionarylanguage_shelf() {
        return dictionarylanguage_shelf;
    }

    public void setDictionarylanguage_shelf(DictionaryLanguage_Shelf dictionarylanguage_shelf) {
        this.dictionarylanguage_shelf = dictionarylanguage_shelf;
    }

}