





import java.util.List;
import java.util.ArrayList;

public class BibTeX_BibTeXFile  {






    private List<BibTeXEntry> bibtexentrys;


    public BibTeX_BibTeXFile(
    ) {
        this.bibtexentrys = new ArrayList<>();
    }

    public BibTeX_BibTeXFile(
        ArrayList<BibTeXEntry> bibtexentrys    ) {
        this.bibtexentrys = bibtexentrys;
    }


    public List<BibTeXEntry> getBibtexentrys() {
        return bibtexentrys;
    }

    public void addBibtexentry(Bibtexentry bibtexentry) {
        this.bibtexentrys.add(bibtexentry);
    }

}