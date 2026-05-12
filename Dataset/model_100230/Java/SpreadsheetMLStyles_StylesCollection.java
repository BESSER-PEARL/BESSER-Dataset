





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_StylesCollection  {






    private Workbook workbook;




    private List<StyleType> styletypes;


    public SpreadsheetMLStyles_StylesCollection(
    ) {
        this.styletypes = new ArrayList<>();
    }

    public SpreadsheetMLStyles_StylesCollection(
        ArrayList<StyleType> styletypes    ) {
        this.styletypes = styletypes;
    }


    public Workbook getWorkbook() {
        return workbook;
    }

    public void setWorkbook(Workbook workbook) {
        this.workbook = workbook;
    }
    public List<StyleType> getStyletypes() {
        return styletypes;
    }

    public void addStyletype(Styletype styletype) {
        this.styletypes.add(styletype);
    }

}