





import java.util.List;
import java.util.ArrayList;

public class bibtex_Proceedings extends BibType {






    private bibtex_Organization bibtex_organization;


    public bibtex_Proceedings(
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

}