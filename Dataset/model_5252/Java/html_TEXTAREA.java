





import java.util.List;
import java.util.ArrayList;

public class html_TEXTAREA  {

    private String cols;
    private String rows;
    private String name;



    public html_TEXTAREA(
        String cols,        String rows,        String name    ) {
        this.cols = cols;
        this.rows = rows;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}