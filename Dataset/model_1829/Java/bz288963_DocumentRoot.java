





import java.util.List;
import java.util.ArrayList;

public class bz288963_DocumentRoot  {

    private String mixed;





    private List<bz288963_Footnote> bz288963_footnotes;




    private List<bz288963_Paragraph> bz288963_paragraphs;




    private List<bz288963_Book> bz288963_books;


    public bz288963_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.bz288963_footnotes = new ArrayList<>();
        this.bz288963_paragraphs = new ArrayList<>();
        this.bz288963_books = new ArrayList<>();
    }

    public bz288963_DocumentRoot(
        String mixed        ArrayList<bz288963_Footnote> bz288963_footnotes,        ArrayList<bz288963_Paragraph> bz288963_paragraphs,        ArrayList<bz288963_Book> bz288963_books    ) {
        this.mixed = mixed;
        this.bz288963_footnotes = bz288963_footnotes;
        this.bz288963_paragraphs = bz288963_paragraphs;
        this.bz288963_books = bz288963_books;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<bz288963_Footnote> getBz288963_footnotes() {
        return bz288963_footnotes;
    }

    public void addBz288963_footnote(Bz288963_footnote bz288963_footnote) {
        this.bz288963_footnotes.add(bz288963_footnote);
    }
    public List<bz288963_Paragraph> getBz288963_paragraphs() {
        return bz288963_paragraphs;
    }

    public void addBz288963_paragraph(Bz288963_paragraph bz288963_paragraph) {
        this.bz288963_paragraphs.add(bz288963_paragraph);
    }
    public List<bz288963_Book> getBz288963_books() {
        return bz288963_books;
    }

    public void addBz288963_book(Bz288963_book bz288963_book) {
        this.bz288963_books.add(bz288963_book);
    }

}