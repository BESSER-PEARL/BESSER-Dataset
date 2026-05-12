





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Column extends ColOrRowElement {

    private String autoFitWidth;
    private String width;





    private Table table;


    public SpreadsheetMLSimplified_Column(
        String autoFitWidth,        String width    ) {
        super(
        );
        this.autoFitWidth = autoFitWidth;
        this.width = width;
    }


    public String getAutofitwidth() {
        return autoFitWidth;
    }

    public void setAutofitwidth(String autoFitWidth) {
        this.autoFitWidth = autoFitWidth;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}