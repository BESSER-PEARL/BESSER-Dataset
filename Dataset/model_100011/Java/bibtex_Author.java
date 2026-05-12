





import java.util.List;
import java.util.ArrayList;

public class bibtex_Author  {

    private String name;
    private String surname;





    private List<bibtex_AuthoredEntry> bibtex_authoredentrys;


    public bibtex_Author(
        String name,        String surname    ) {
        this.name = name;
        this.surname = surname;
        this.bibtex_authoredentrys = new ArrayList<>();
    }

    public bibtex_Author(
        String name,        String surname        ArrayList<bibtex_AuthoredEntry> bibtex_authoredentrys    ) {
        this.name = name;
        this.surname = surname;
        this.bibtex_authoredentrys = bibtex_authoredentrys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public List<bibtex_AuthoredEntry> getBibtex_authoredentrys() {
        return bibtex_authoredentrys;
    }

    public void addBibtex_authoredentry(Bibtex_authoredentry bibtex_authoredentry) {
        this.bibtex_authoredentrys.add(bibtex_authoredentry);
    }

}