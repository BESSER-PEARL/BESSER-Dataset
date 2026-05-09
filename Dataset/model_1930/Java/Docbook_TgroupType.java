





import java.util.List;
import java.util.ArrayList;

public class Docbook_TgroupType  {

    private String rowseq;
    private String cols;
    private String colseq;
    private String align;





    private Docbook_TableType docbook_tabletype;




    private Docbook_TbodyType docbook_tbodytype;




    private List<Docbook_ColspecType> docbook_colspectypes;




    private Docbook_InformaltableType docbook_informaltabletype;




    private Docbook_DocumentRoot docbook_documentroot;


    public Docbook_TgroupType(
        String rowseq,        String cols,        String colseq,        String align    ) {
        this.rowseq = rowseq;
        this.cols = cols;
        this.colseq = colseq;
        this.align = align;
        this.docbook_colspectypes = new ArrayList<>();
    }

    public Docbook_TgroupType(
        String rowseq,        String cols,        String colseq,        String align        ArrayList<Docbook_ColspecType> docbook_colspectypes    ) {
        this.rowseq = rowseq;
        this.cols = cols;
        this.colseq = colseq;
        this.align = align;
        this.docbook_colspectypes = docbook_colspectypes;
    }

    public String getRowseq() {
        return rowseq;
    }

    public void setRowseq(String rowseq) {
        this.rowseq = rowseq;
    }
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }
    public String getColseq() {
        return colseq;
    }

    public void setColseq(String colseq) {
        this.colseq = colseq;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }

    public Docbook_TableType getDocbook_tabletype() {
        return docbook_tabletype;
    }

    public void setDocbook_tabletype(Docbook_TableType docbook_tabletype) {
        this.docbook_tabletype = docbook_tabletype;
    }
    public Docbook_TbodyType getDocbook_tbodytype() {
        return docbook_tbodytype;
    }

    public void setDocbook_tbodytype(Docbook_TbodyType docbook_tbodytype) {
        this.docbook_tbodytype = docbook_tbodytype;
    }
    public List<Docbook_ColspecType> getDocbook_colspectypes() {
        return docbook_colspectypes;
    }

    public void addDocbook_colspectype(Docbook_colspectype docbook_colspectype) {
        this.docbook_colspectypes.add(docbook_colspectype);
    }
    public Docbook_InformaltableType getDocbook_informaltabletype() {
        return docbook_informaltabletype;
    }

    public void setDocbook_informaltabletype(Docbook_InformaltableType docbook_informaltabletype) {
        this.docbook_informaltabletype = docbook_informaltabletype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }

}