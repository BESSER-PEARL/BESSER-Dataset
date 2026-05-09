





import java.util.List;
import java.util.ArrayList;

public class Docbook_ColspecType  {

    private String colname;
    private String colwidth;



    public Docbook_ColspecType(
        String colname,        String colwidth    ) {
        this.colname = colname;
        this.colwidth = colwidth;
    }


    public String getColname() {
        return colname;
    }

    public void setColname(String colname) {
        this.colname = colname;
    }
    public String getColwidth() {
        return colwidth;
    }

    public void setColwidth(String colwidth) {
        this.colwidth = colwidth;
    }


}