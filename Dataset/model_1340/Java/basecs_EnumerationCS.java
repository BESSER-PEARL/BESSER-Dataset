





import java.util.List;
import java.util.ArrayList;

public class basecs_EnumerationCS extends NamespaceCS, ClassifierCS {






    private List<basecs_EnumerationLiteralCS> basecs_enumerationliteralcss;


    public basecs_EnumerationCS(
    ) {
        super(
        );
        this.basecs_enumerationliteralcss = new ArrayList<>();
    }

    public basecs_EnumerationCS(
        ArrayList<basecs_EnumerationLiteralCS> basecs_enumerationliteralcss    ) {
        this.basecs_enumerationliteralcss = basecs_enumerationliteralcss;
    }


    public List<basecs_EnumerationLiteralCS> getBasecs_enumerationliteralcss() {
        return basecs_enumerationliteralcss;
    }

    public void addBasecs_enumerationliteralcs(Basecs_enumerationliteralcs basecs_enumerationliteralcs) {
        this.basecs_enumerationliteralcss.add(basecs_enumerationliteralcs);
    }

}