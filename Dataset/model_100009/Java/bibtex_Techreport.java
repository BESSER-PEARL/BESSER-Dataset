





import java.util.List;
import java.util.ArrayList;

public class bibtex_Techreport extends BibType {






    private bibtex_Type bibtex_type;




    private bibtex_Institution bibtex_institution;


    public bibtex_Techreport(
    ) {
        super(
        );
    }



    public bibtex_Type getBibtex_type() {
        return bibtex_type;
    }

    public void setBibtex_type(bibtex_Type bibtex_type) {
        this.bibtex_type = bibtex_type;
    }
    public bibtex_Institution getBibtex_institution() {
        return bibtex_institution;
    }

    public void setBibtex_institution(bibtex_Institution bibtex_institution) {
        this.bibtex_institution = bibtex_institution;
    }

}