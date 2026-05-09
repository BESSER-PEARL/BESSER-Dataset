





import java.util.List;
import java.util.ArrayList;

public class cellsheet_Sheet extends HasId, HasA1 {

    private int sheetIndex;
    private String sheetName;





    private cellsheet_Book cellsheet_book;




    private cellsheet_Book cellsheet_book;


    public cellsheet_Sheet(
        int sheetIndex,        String sheetName    ) {
        super(
        );
        this.sheetIndex = sheetIndex;
        this.sheetName = sheetName;
    }


    public int getSheetindex() {
        return sheetIndex;
    }

    public void setSheetindex(int sheetIndex) {
        this.sheetIndex = sheetIndex;
    }
    public String getSheetname() {
        return sheetName;
    }

    public void setSheetname(String sheetName) {
        this.sheetName = sheetName;
    }

    public cellsheet_Book getCellsheet_book() {
        return cellsheet_book;
    }

    public void setCellsheet_book(cellsheet_Book cellsheet_book) {
        this.cellsheet_book = cellsheet_book;
    }
    public cellsheet_Book getCellsheet_book() {
        return cellsheet_book;
    }

    public void setCellsheet_book(cellsheet_Book cellsheet_book) {
        this.cellsheet_book = cellsheet_book;
    }

}