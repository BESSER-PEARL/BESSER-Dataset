





import java.util.List;
import java.util.ArrayList;

public class bibtex_AbstractField extends StringValue, Field {






    private bibtex_Entry bibtex_entry;


    public bibtex_AbstractField(
    ) {
        super(
        );
    }



    public bibtex_Entry getBibtex_entry() {
        return bibtex_entry;
    }

    public void setBibtex_entry(bibtex_Entry bibtex_entry) {
        this.bibtex_entry = bibtex_entry;
    }

}