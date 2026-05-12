





import java.util.List;
import java.util.ArrayList;

public class Library_Management_System_Librarian  {

    private String LibrarianName;





    private List<Library_Management_System_Patron> library_management_system_patrons;


    public Library_Management_System_Librarian(
        String LibrarianName    ) {
        this.LibrarianName = LibrarianName;
        this.library_management_system_patrons = new ArrayList<>();
    }

    public Library_Management_System_Librarian(
        String LibrarianName        ArrayList<Library_Management_System_Patron> library_management_system_patrons    ) {
        this.LibrarianName = LibrarianName;
        this.library_management_system_patrons = library_management_system_patrons;
    }

    public String getLibrarianname() {
        return LibrarianName;
    }

    public void setLibrarianname(String LibrarianName) {
        this.LibrarianName = LibrarianName;
    }

    public List<Library_Management_System_Patron> getLibrary_management_system_patrons() {
        return library_management_system_patrons;
    }

    public void addLibrary_management_system_patron(Library_management_system_patron library_management_system_patron) {
        this.library_management_system_patrons.add(library_management_system_patron);
    }

}