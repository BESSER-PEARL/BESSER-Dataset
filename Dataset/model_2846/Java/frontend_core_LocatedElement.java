





import java.util.List;
import java.util.ArrayList;

public class frontend_core_LocatedElement  {

    private int row;
    private int column;
    private String file;



    public frontend_core_LocatedElement(
        int row,        int column,        String file    ) {
        this.row = row;
        this.column = column;
        this.file = file;
    }


    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }
    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}