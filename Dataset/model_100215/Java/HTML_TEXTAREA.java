





import java.util.List;
import java.util.ArrayList;

public class HTML_TEXTAREA  {

    private String name;
    private String cols;
    private String rows;



    public HTML_TEXTAREA(
        String name,        String cols,        String rows    ) {
        this.name = name;
        this.cols = cols;
        this.rows = rows;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }
    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }


}