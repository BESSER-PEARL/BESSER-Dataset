





import java.util.List;
import java.util.ArrayList;

public class core_LocatedElement  {

    private int row;
    private String file;
    private int column;



    public core_LocatedElement(
        int row,        String file,        int column    ) {
        this.row = row;
        this.file = file;
        this.column = column;
    }


    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }


}