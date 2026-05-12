





import java.util.List;
import java.util.ArrayList;

public class bibtex_Inbook extends BibType {

    private boolean editor;
    private boolean author;





    private bibtex_Chapter bibtex_chapter;


    public bibtex_Inbook(
        boolean editor,        boolean author    ) {
        super(
        );
        this.editor = editor;
        this.author = author;
    }


    public boolean getEditor() {
        return editor;
    }

    public void setEditor(boolean editor) {
        this.editor = editor;
    }
    public boolean getAuthor() {
        return author;
    }

    public void setAuthor(boolean author) {
        this.author = author;
    }

    public bibtex_Chapter getBibtex_chapter() {
        return bibtex_chapter;
    }

    public void setBibtex_chapter(bibtex_Chapter bibtex_chapter) {
        this.bibtex_chapter = bibtex_chapter;
    }

}