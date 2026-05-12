





import java.util.List;
import java.util.ArrayList;

public class bibtex_Editor  {

    private String editor;





    private bibtex_Book bibtex_book;




    private bibtex_Proceedings bibtex_proceedings;




    private bibtex_Conference bibtex_conference;




    private bibtex_Inproceedings bibtex_inproceedings;




    private bibtex_Incollection bibtex_incollection;


    public bibtex_Editor(
        String editor    ) {
        this.editor = editor;
    }


    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }

    public bibtex_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibtex_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }
    public bibtex_Proceedings getBibtex_proceedings() {
        return bibtex_proceedings;
    }

    public void setBibtex_proceedings(bibtex_Proceedings bibtex_proceedings) {
        this.bibtex_proceedings = bibtex_proceedings;
    }
    public bibtex_Conference getBibtex_conference() {
        return bibtex_conference;
    }

    public void setBibtex_conference(bibtex_Conference bibtex_conference) {
        this.bibtex_conference = bibtex_conference;
    }
    public bibtex_Inproceedings getBibtex_inproceedings() {
        return bibtex_inproceedings;
    }

    public void setBibtex_inproceedings(bibtex_Inproceedings bibtex_inproceedings) {
        this.bibtex_inproceedings = bibtex_inproceedings;
    }
    public bibtex_Incollection getBibtex_incollection() {
        return bibtex_incollection;
    }

    public void setBibtex_incollection(bibtex_Incollection bibtex_incollection) {
        this.bibtex_incollection = bibtex_incollection;
    }

}