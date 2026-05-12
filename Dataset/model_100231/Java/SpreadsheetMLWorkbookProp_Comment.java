





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_Comment  {

    private String showAlways;
    private String author;





    private Data data;




    private Cell cell;


    public SpreadsheetMLWorkbookProp_Comment(
        String showAlways,        String author    ) {
        this.showAlways = showAlways;
        this.author = author;
    }


    public String getShowalways() {
        return showAlways;
    }

    public void setShowalways(String showAlways) {
        this.showAlways = showAlways;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public Data getData() {
        return data;
    }

    public void setData(Data data) {
        this.data = data;
    }
    public Cell getCell() {
        return cell;
    }

    public void setCell(Cell cell) {
        this.cell = cell;
    }

}