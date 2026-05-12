





import java.util.List;
import java.util.ArrayList;

public class bibtex_Booktitle  {

    private String booktitle;





    private bibtex_Conference bibtex_conference;


    public bibtex_Booktitle(
        String booktitle    ) {
        this.booktitle = booktitle;
    }


    public String getBooktitle() {
        return booktitle;
    }

    public void setBooktitle(String booktitle) {
        this.booktitle = booktitle;
    }

    public bibtex_Conference getBibtex_conference() {
        return bibtex_conference;
    }

    public void setBibtex_conference(bibtex_Conference bibtex_conference) {
        this.bibtex_conference = bibtex_conference;
    }

}