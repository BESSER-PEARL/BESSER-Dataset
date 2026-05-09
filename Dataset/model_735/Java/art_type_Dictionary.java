





import java.util.List;
import java.util.ArrayList;

public class art_type_Dictionary extends Attribute {






    private List<DictionaryDefaultValue> dictionarydefaultvalues;


    public art_type_Dictionary(
    ) {
        super(
        );
        this.dictionarydefaultvalues = new ArrayList<>();
    }

    public art_type_Dictionary(
        ArrayList<DictionaryDefaultValue> dictionarydefaultvalues    ) {
        this.dictionarydefaultvalues = dictionarydefaultvalues;
    }


    public List<DictionaryDefaultValue> getDictionarydefaultvalues() {
        return dictionarydefaultvalues;
    }

    public void addDictionarydefaultvalue(Dictionarydefaultvalue dictionarydefaultvalue) {
        this.dictionarydefaultvalues.add(dictionarydefaultvalue);
    }

}