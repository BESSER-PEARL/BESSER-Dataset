





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Author  {

    private String fullBio;
    private String name;
    private String nationality;





    private libraryinteractionmodel_AuthorShort libraryinteractionmodel_authorshort;




    private List<libraryinteractionmodel_BookShort> libraryinteractionmodel_bookshorts;


    public libraryinteractionmodel_Author(
        String fullBio,        String name,        String nationality    ) {
        this.fullBio = fullBio;
        this.name = name;
        this.nationality = nationality;
        this.libraryinteractionmodel_bookshorts = new ArrayList<>();
    }

    public libraryinteractionmodel_Author(
        String fullBio,        String name,        String nationality        ArrayList<libraryinteractionmodel_BookShort> libraryinteractionmodel_bookshorts    ) {
        this.fullBio = fullBio;
        this.name = name;
        this.nationality = nationality;
        this.libraryinteractionmodel_bookshorts = libraryinteractionmodel_bookshorts;
    }

    public String getFullbio() {
        return fullBio;
    }

    public void setFullbio(String fullBio) {
        this.fullBio = fullBio;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }

    public libraryinteractionmodel_AuthorShort getLibraryinteractionmodel_authorshort() {
        return libraryinteractionmodel_authorshort;
    }

    public void setLibraryinteractionmodel_authorshort(libraryinteractionmodel_AuthorShort libraryinteractionmodel_authorshort) {
        this.libraryinteractionmodel_authorshort = libraryinteractionmodel_authorshort;
    }
    public List<libraryinteractionmodel_BookShort> getLibraryinteractionmodel_bookshorts() {
        return libraryinteractionmodel_bookshorts;
    }

    public void addLibraryinteractionmodel_bookshort(Libraryinteractionmodel_bookshort libraryinteractionmodel_bookshort) {
        this.libraryinteractionmodel_bookshorts.add(libraryinteractionmodel_bookshort);
    }

}