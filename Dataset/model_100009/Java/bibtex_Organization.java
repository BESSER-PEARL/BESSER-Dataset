





import java.util.List;
import java.util.ArrayList;

public class bibtex_Organization  {

    private String organization;





    private bibtex_Conference bibtex_conference;


    public bibtex_Organization(
        String organization    ) {
        this.organization = organization;
    }


    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }

    public bibtex_Conference getBibtex_conference() {
        return bibtex_conference;
    }

    public void setBibtex_conference(bibtex_Conference bibtex_conference) {
        this.bibtex_conference = bibtex_conference;
    }

}