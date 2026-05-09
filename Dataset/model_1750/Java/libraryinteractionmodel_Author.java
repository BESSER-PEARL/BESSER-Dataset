





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Author  {

    private String nationality;
    private String name;
    private String fullBio;





    private List<libraryinteractionmodel_BookShort> libraryinteractionmodel_bookshorts;


    public libraryinteractionmodel_Author(
        String nationality,        String name,        String fullBio    ) {
        this.nationality = nationality;
        this.name = name;
        this.fullBio = fullBio;
        this.libraryinteractionmodel_bookshorts = new ArrayList<>();
    }

    public libraryinteractionmodel_Author(
        String nationality,        String name,        String fullBio        ArrayList<libraryinteractionmodel_BookShort> libraryinteractionmodel_bookshorts    ) {
        this.nationality = nationality;
        this.name = name;
        this.fullBio = fullBio;
        this.libraryinteractionmodel_bookshorts = libraryinteractionmodel_bookshorts;
    }

    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFullbio() {
        return fullBio;
    }

    public void setFullbio(String fullBio) {
        this.fullBio = fullBio;
    }

    public List<libraryinteractionmodel_BookShort> getLibraryinteractionmodel_bookshorts() {
        return libraryinteractionmodel_bookshorts;
    }

    public void addLibraryinteractionmodel_bookshort(Libraryinteractionmodel_bookshort libraryinteractionmodel_bookshort) {
        this.libraryinteractionmodel_bookshorts.add(libraryinteractionmodel_bookshort);
    }

}