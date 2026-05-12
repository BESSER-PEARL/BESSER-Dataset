





import java.util.List;
import java.util.ArrayList;

public class bibTeX_NoteField  {

    private String note;





    private bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes;


    public bibTeX_NoteField(
        String note    ) {
        this.note = note;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public bibTeX_BibtexEntryTypes getBibtex_bibtexentrytypes() {
        return bibtex_bibtexentrytypes;
    }

    public void setBibtex_bibtexentrytypes(bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes) {
        this.bibtex_bibtexentrytypes = bibtex_bibtexentrytypes;
    }

}