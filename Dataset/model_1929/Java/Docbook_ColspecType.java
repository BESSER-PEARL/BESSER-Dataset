





import java.util.List;
import java.util.ArrayList;

public class Docbook_ColspecType  {

    private String colwidth;
    private String colname;



    public Docbook_ColspecType(
        String colwidth,        String colname    ) {
        this.colwidth = colwidth;
        this.colname = colname;
    }


    public String getColwidth() {
        return colwidth;
    }

    public void setColwidth(String colwidth) {
        this.colwidth = colwidth;
    }
    public String getColname() {
        return colname;
    }

    public void setColname(String colname) {
        this.colname = colname;
    }


}