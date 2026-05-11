





import java.util.List;
import java.util.ArrayList;

public class dsml_web_TextArea extends Field {

    private int cols;
    private int rows;



    public dsml_web_TextArea(
        int cols,        int rows    ) {
        super(
        );
        this.cols = cols;
        this.rows = rows;
    }


    public int getCols() {
        return cols;
    }

    public void setCols(int cols) {
        this.cols = cols;
    }
    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }


}