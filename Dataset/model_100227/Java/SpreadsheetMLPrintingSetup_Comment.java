





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_Comment  {

    private String author;
    private String showAlways;





    private Cell cell;


    public SpreadsheetMLPrintingSetup_Comment(
        String author,        String showAlways    ) {
        this.author = author;
        this.showAlways = showAlways;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getShowalways() {
        return showAlways;
    }

    public void setShowalways(String showAlways) {
        this.showAlways = showAlways;
    }

    public Cell getCell() {
        return cell;
    }

    public void setCell(Cell cell) {
        this.cell = cell;
    }

}