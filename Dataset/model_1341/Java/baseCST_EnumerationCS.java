





import java.util.List;
import java.util.ArrayList;

public class baseCST_EnumerationCS extends NamespaceCS, ClassifierCS {






    private List<baseCST_EnumerationLiteralCS> basecst_enumerationliteralcss;


    public baseCST_EnumerationCS(
    ) {
        super(
        );
        this.basecst_enumerationliteralcss = new ArrayList<>();
    }

    public baseCST_EnumerationCS(
        ArrayList<baseCST_EnumerationLiteralCS> basecst_enumerationliteralcss    ) {
        this.basecst_enumerationliteralcss = basecst_enumerationliteralcss;
    }


    public List<baseCST_EnumerationLiteralCS> getBasecst_enumerationliteralcss() {
        return basecst_enumerationliteralcss;
    }

    public void addBasecst_enumerationliteralcs(Basecst_enumerationliteralcs basecst_enumerationliteralcs) {
        this.basecst_enumerationliteralcss.add(basecst_enumerationliteralcs);
    }

}