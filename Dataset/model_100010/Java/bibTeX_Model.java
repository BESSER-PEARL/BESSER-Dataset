





import java.util.List;
import java.util.ArrayList;

public class bibTeX_Model  {






    private List<bibTeX_BibtexEntryTypes> bibtex_bibtexentrytypess;


    public bibTeX_Model(
    ) {
        this.bibtex_bibtexentrytypess = new ArrayList<>();
    }

    public bibTeX_Model(
        ArrayList<bibTeX_BibtexEntryTypes> bibtex_bibtexentrytypess    ) {
        this.bibtex_bibtexentrytypess = bibtex_bibtexentrytypess;
    }


    public List<bibTeX_BibtexEntryTypes> getBibtex_bibtexentrytypess() {
        return bibtex_bibtexentrytypess;
    }

    public void addBibtex_bibtexentrytypes(Bibtex_bibtexentrytypes bibtex_bibtexentrytypes) {
        this.bibtex_bibtexentrytypess.add(bibtex_bibtexentrytypes);
    }

}