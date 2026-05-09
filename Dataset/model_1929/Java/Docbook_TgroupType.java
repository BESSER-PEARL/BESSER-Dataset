





import java.util.List;
import java.util.ArrayList;

public class Docbook_TgroupType  {

    private String align;
    private String rowseq;
    private String colseq;
    private String cols;





    private Docbook_TableType docbook_tabletype;




    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_InformaltableType docbook_informaltabletype;




    private List<Docbook_ColspecType> docbook_colspectypes;




    private Docbook_TbodyType docbook_tbodytype;


    public Docbook_TgroupType(
        String align,        String rowseq,        String colseq,        String cols    ) {
        this.align = align;
        this.rowseq = rowseq;
        this.colseq = colseq;
        this.cols = cols;
        this.docbook_colspectypes = new ArrayList<>();
    }

    public Docbook_TgroupType(
        String align,        String rowseq,        String colseq,        String cols        ArrayList<Docbook_ColspecType> docbook_colspectypes    ) {
        this.align = align;
        this.rowseq = rowseq;
        this.colseq = colseq;
        this.cols = cols;
        this.docbook_colspectypes = docbook_colspectypes;
    }

    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getRowseq() {
        return rowseq;
    }

    public void setRowseq(String rowseq) {
        this.rowseq = rowseq;
    }
    public String getColseq() {
        return colseq;
    }

    public void setColseq(String colseq) {
        this.colseq = colseq;
    }
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }

    public Docbook_TableType getDocbook_tabletype() {
        return docbook_tabletype;
    }

    public void setDocbook_tabletype(Docbook_TableType docbook_tabletype) {
        this.docbook_tabletype = docbook_tabletype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_InformaltableType getDocbook_informaltabletype() {
        return docbook_informaltabletype;
    }

    public void setDocbook_informaltabletype(Docbook_InformaltableType docbook_informaltabletype) {
        this.docbook_informaltabletype = docbook_informaltabletype;
    }
    public List<Docbook_ColspecType> getDocbook_colspectypes() {
        return docbook_colspectypes;
    }

    public void addDocbook_colspectype(Docbook_colspectype docbook_colspectype) {
        this.docbook_colspectypes.add(docbook_colspectype);
    }
    public Docbook_TbodyType getDocbook_tbodytype() {
        return docbook_tbodytype;
    }

    public void setDocbook_tbodytype(Docbook_TbodyType docbook_tbodytype) {
        this.docbook_tbodytype = docbook_tbodytype;
    }

}