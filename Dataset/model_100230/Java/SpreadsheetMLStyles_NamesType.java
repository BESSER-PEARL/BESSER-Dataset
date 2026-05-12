





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_NamesType  {






    private List<NamedRange> namedranges;




    private Workbook workbook;


    public SpreadsheetMLStyles_NamesType(
    ) {
        this.namedranges = new ArrayList<>();
    }

    public SpreadsheetMLStyles_NamesType(
        ArrayList<NamedRange> namedranges    ) {
        this.namedranges = namedranges;
    }


    public List<NamedRange> getNamedranges() {
        return namedranges;
    }

    public void addNamedrange(Namedrange namedrange) {
        this.namedranges.add(namedrange);
    }
    public Workbook getWorkbook() {
        return workbook;
    }

    public void setWorkbook(Workbook workbook) {
        this.workbook = workbook;
    }

}