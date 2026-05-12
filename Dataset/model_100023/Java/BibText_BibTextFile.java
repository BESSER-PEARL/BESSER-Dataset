





import java.util.List;
import java.util.ArrayList;

public class BibText_BibTextFile  {






    private List<BibText_BibTextEntry> bibtext_bibtextentrys;


    public BibText_BibTextFile(
    ) {
        this.bibtext_bibtextentrys = new ArrayList<>();
    }

    public BibText_BibTextFile(
        ArrayList<BibText_BibTextEntry> bibtext_bibtextentrys    ) {
        this.bibtext_bibtextentrys = bibtext_bibtextentrys;
    }


    public List<BibText_BibTextEntry> getBibtext_bibtextentrys() {
        return bibtext_bibtextentrys;
    }

    public void addBibtext_bibtextentry(Bibtext_bibtextentry bibtext_bibtextentry) {
        this.bibtext_bibtextentrys.add(bibtext_bibtextentry);
    }

}