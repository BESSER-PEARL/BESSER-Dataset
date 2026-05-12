





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Row extends ColOrRowElement {

    private String height;
    private String autoFitHeight;





    private Table table;


    public SpreadsheetMLSimplified_Row(
        String height,        String autoFitHeight    ) {
        super(
        );
        this.height = height;
        this.autoFitHeight = autoFitHeight;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getAutofitheight() {
        return autoFitHeight;
    }

    public void setAutofitheight(String autoFitHeight) {
        this.autoFitHeight = autoFitHeight;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}