





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_Column extends ColOrRowElement {

    private String width;
    private String autoFitWidth;





    private Table table;


    public SpreadsheetMLPrintingSetup_Column(
        String width,        String autoFitWidth    ) {
        super(
        );
        this.width = width;
        this.autoFitWidth = autoFitWidth;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAutofitwidth() {
        return autoFitWidth;
    }

    public void setAutofitwidth(String autoFitWidth) {
        this.autoFitWidth = autoFitWidth;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}