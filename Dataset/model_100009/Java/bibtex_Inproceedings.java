





import java.util.List;
import java.util.ArrayList;

public class bibtex_Inproceedings extends BibType {






    private bibtex_Organization bibtex_organization;




    private bibtex_Booktitle bibtex_booktitle;


    public bibtex_Inproceedings(
    ) {
        super(
        );
    }



    public bibtex_Organization getBibtex_organization() {
        return bibtex_organization;
    }

    public void setBibtex_organization(bibtex_Organization bibtex_organization) {
        this.bibtex_organization = bibtex_organization;
    }
    public bibtex_Booktitle getBibtex_booktitle() {
        return bibtex_booktitle;
    }

    public void setBibtex_booktitle(bibtex_Booktitle bibtex_booktitle) {
        this.bibtex_booktitle = bibtex_booktitle;
    }

}