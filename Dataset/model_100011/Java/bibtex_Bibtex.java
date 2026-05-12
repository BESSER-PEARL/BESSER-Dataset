





import java.util.List;
import java.util.ArrayList;

public class bibtex_Bibtex  {






    private List<bibtex_Entries> bibtex_entriess;


    public bibtex_Bibtex(
    ) {
        this.bibtex_entriess = new ArrayList<>();
    }

    public bibtex_Bibtex(
        ArrayList<bibtex_Entries> bibtex_entriess    ) {
        this.bibtex_entriess = bibtex_entriess;
    }


    public List<bibtex_Entries> getBibtex_entriess() {
        return bibtex_entriess;
    }

    public void addBibtex_entries(Bibtex_entries bibtex_entries) {
        this.bibtex_entriess.add(bibtex_entries);
    }

}