





import java.util.List;
import java.util.ArrayList;

public class Library_Management_System_Faculty  {

    private int FacultyId;
    private String FacultyName;





    private List<Library_Management_System_Patron> library_management_system_patrons;


    public Library_Management_System_Faculty(
        int FacultyId,        String FacultyName    ) {
        this.FacultyId = FacultyId;
        this.FacultyName = FacultyName;
        this.library_management_system_patrons = new ArrayList<>();
    }

    public Library_Management_System_Faculty(
        int FacultyId,        String FacultyName        ArrayList<Library_Management_System_Patron> library_management_system_patrons    ) {
        this.FacultyId = FacultyId;
        this.FacultyName = FacultyName;
        this.library_management_system_patrons = library_management_system_patrons;
    }

    public int getFacultyid() {
        return FacultyId;
    }

    public void setFacultyid(int FacultyId) {
        this.FacultyId = FacultyId;
    }
    public String getFacultyname() {
        return FacultyName;
    }

    public void setFacultyname(String FacultyName) {
        this.FacultyName = FacultyName;
    }

    public List<Library_Management_System_Patron> getLibrary_management_system_patrons() {
        return library_management_system_patrons;
    }

    public void addLibrary_management_system_patron(Library_management_system_patron library_management_system_patron) {
        this.library_management_system_patrons.add(library_management_system_patron);
    }

}