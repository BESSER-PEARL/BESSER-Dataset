





import java.util.List;
import java.util.ArrayList;

public class bibtex_Bibliography  {






    private List<bibtex_Entry> bibtex_entrys;


    public bibtex_Bibliography(
    ) {
        this.bibtex_entrys = new ArrayList<>();
    }

    public bibtex_Bibliography(
        ArrayList<bibtex_Entry> bibtex_entrys    ) {
        this.bibtex_entrys = bibtex_entrys;
    }


    public List<bibtex_Entry> getBibtex_entrys() {
        return bibtex_entrys;
    }

    public void addBibtex_entry(Bibtex_entry bibtex_entry) {
        this.bibtex_entrys.add(bibtex_entry);
    }

}