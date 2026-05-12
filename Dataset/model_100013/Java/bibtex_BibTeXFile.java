





import java.util.List;
import java.util.ArrayList;

public class bibtex_BibTeXFile  {






    private List<bibtex_BibTeXEntry> bibtex_bibtexentrys;


    public bibtex_BibTeXFile(
    ) {
        this.bibtex_bibtexentrys = new ArrayList<>();
    }

    public bibtex_BibTeXFile(
        ArrayList<bibtex_BibTeXEntry> bibtex_bibtexentrys    ) {
        this.bibtex_bibtexentrys = bibtex_bibtexentrys;
    }


    public List<bibtex_BibTeXEntry> getBibtex_bibtexentrys() {
        return bibtex_bibtexentrys;
    }

    public void addBibtex_bibtexentry(Bibtex_bibtexentry bibtex_bibtexentry) {
        this.bibtex_bibtexentrys.add(bibtex_bibtexentry);
    }

}