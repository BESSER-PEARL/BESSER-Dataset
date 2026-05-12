





import java.util.List;
import java.util.ArrayList;

public class Library_Management_System_Faculty  {

    private String FacultyName;
    private int FacultyId;





    private List<Library_Management_System_Patron> library_management_system_patrons;


    public Library_Management_System_Faculty(
        String FacultyName,        int FacultyId    ) {
        this.FacultyName = FacultyName;
        this.FacultyId = FacultyId;
        this.library_management_system_patrons = new ArrayList<>();
    }

    public Library_Management_System_Faculty(
        String FacultyName,        int FacultyId        ArrayList<Library_Management_System_Patron> library_management_system_patrons    ) {
        this.FacultyName = FacultyName;
        this.FacultyId = FacultyId;
        this.library_management_system_patrons = library_management_system_patrons;
    }

    public String getFacultyname() {
        return FacultyName;
    }

    public void setFacultyname(String FacultyName) {
        this.FacultyName = FacultyName;
    }
    public int getFacultyid() {
        return FacultyId;
    }

    public void setFacultyid(int FacultyId) {
        this.FacultyId = FacultyId;
    }

    public List<Library_Management_System_Patron> getLibrary_management_system_patrons() {
        return library_management_system_patrons;
    }

    public void addLibrary_management_system_patron(Library_management_system_patron library_management_system_patron) {
        this.library_management_system_patrons.add(library_management_system_patron);
    }

}