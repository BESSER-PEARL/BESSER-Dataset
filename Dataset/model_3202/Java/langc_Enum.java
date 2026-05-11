





import java.util.List;
import java.util.ArrayList;

public class langc_Enum extends NamedElement {






    private List<langc_Enumerator> langc_enumerators;


    public langc_Enum(
    ) {
        super(
        );
        this.langc_enumerators = new ArrayList<>();
    }

    public langc_Enum(
        ArrayList<langc_Enumerator> langc_enumerators    ) {
        this.langc_enumerators = langc_enumerators;
    }


    public List<langc_Enumerator> getLangc_enumerators() {
        return langc_enumerators;
    }

    public void addLangc_enumerator(Langc_enumerator langc_enumerator) {
        this.langc_enumerators.add(langc_enumerator);
    }

}