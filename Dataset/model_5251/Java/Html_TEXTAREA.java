





import java.util.List;
import java.util.ArrayList;

public class Html_TEXTAREA  {

    private String name;
    private String rows;
    private String cols;



    public Html_TEXTAREA(
        String name,        String rows,        String cols    ) {
        this.name = name;
        this.rows = rows;
        this.cols = cols;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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


}