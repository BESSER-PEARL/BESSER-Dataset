





import java.util.List;
import java.util.ArrayList;

public class DictionaryLanguage_Shelf  {

    private String description;





    private DictionaryLanguage_Library dictionarylanguage_library;


    public DictionaryLanguage_Shelf(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public DictionaryLanguage_Library getDictionarylanguage_library() {
        return dictionarylanguage_library;
    }

    public void setDictionarylanguage_library(DictionaryLanguage_Library dictionarylanguage_library) {
        this.dictionarylanguage_library = dictionarylanguage_library;
    }

}