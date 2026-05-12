





import java.util.List;
import java.util.ArrayList;

public class HTML_TEXTAREA  {

    private String rows;
    private String cols;
    private String name;



    public HTML_TEXTAREA(
        String rows,        String cols,        String name    ) {
        this.rows = rows;
        this.cols = cols;
        this.name = name;
    }


    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}