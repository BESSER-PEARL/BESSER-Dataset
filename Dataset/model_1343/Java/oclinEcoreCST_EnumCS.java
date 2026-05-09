





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_EnumCS extends DataTypeOrEnumCS {






    private List<oclinEcoreCST_EnumLiteralCS> oclinecorecst_enumliteralcss;


    public oclinEcoreCST_EnumCS(
    ) {
        super(
        );
        this.oclinecorecst_enumliteralcss = new ArrayList<>();
    }

    public oclinEcoreCST_EnumCS(
        ArrayList<oclinEcoreCST_EnumLiteralCS> oclinecorecst_enumliteralcss    ) {
        this.oclinecorecst_enumliteralcss = oclinecorecst_enumliteralcss;
    }


    public List<oclinEcoreCST_EnumLiteralCS> getOclinecorecst_enumliteralcss() {
        return oclinecorecst_enumliteralcss;
    }

    public void addOclinecorecst_enumliteralcs(Oclinecorecst_enumliteralcs oclinecorecst_enumliteralcs) {
        this.oclinecorecst_enumliteralcss.add(oclinecorecst_enumliteralcs);
    }

}