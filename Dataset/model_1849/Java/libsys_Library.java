





import java.util.List;
import java.util.ArrayList;

public class libsys_Library  {






    private List<libsys_Librarian> libsys_librarians;




    private libsys_User libsys_user;




    private List<libsys_Medium> libsys_mediums;


    public libsys_Library(
    ) {
        this.libsys_librarians = new ArrayList<>();
        this.libsys_mediums = new ArrayList<>();
    }

    public libsys_Library(
        ArrayList<libsys_Librarian> libsys_librarians,        ArrayList<libsys_Medium> libsys_mediums    ) {
        this.libsys_librarians = libsys_librarians;
        this.libsys_mediums = libsys_mediums;
    }


    public List<libsys_Librarian> getLibsys_librarians() {
        return libsys_librarians;
    }

    public void addLibsys_librarian(Libsys_librarian libsys_librarian) {
        this.libsys_librarians.add(libsys_librarian);
    }
    public libsys_User getLibsys_user() {
        return libsys_user;
    }

    public void setLibsys_user(libsys_User libsys_user) {
        this.libsys_user = libsys_user;
    }
    public List<libsys_Medium> getLibsys_mediums() {
        return libsys_mediums;
    }

    public void addLibsys_medium(Libsys_medium libsys_medium) {
        this.libsys_mediums.add(libsys_medium);
    }

}