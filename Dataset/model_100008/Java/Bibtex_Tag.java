





import java.util.List;
import java.util.ArrayList;

public class Bibtex_Tag  {

    private String Name;





    private Bibtex_BibtexEntry bibtex_bibtexentry;


    public Bibtex_Tag(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Bibtex_BibtexEntry getBibtex_bibtexentry() {
        return bibtex_bibtexentry;
    }

    public void setBibtex_bibtexentry(Bibtex_BibtexEntry bibtex_bibtexentry) {
        this.bibtex_bibtexentry = bibtex_bibtexentry;
    }

}