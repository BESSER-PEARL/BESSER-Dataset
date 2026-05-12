





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_Comment  {

    private String author;
    private String showAlways;





    private Data data;




    private Cell cell;


    public SpreadsheetMLStyles_Comment(
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