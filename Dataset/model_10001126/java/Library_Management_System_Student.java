





import java.util.List;
import java.util.ArrayList;

public class Library_Management_System_Student  {

    private int StudentId;
    private String StudentName;





    private List<Library_Management_System_Patron> library_management_system_patrons;


    public Library_Management_System_Student(
        int StudentId,        String StudentName    ) {
        this.StudentId = StudentId;
        this.StudentName = StudentName;
        this.library_management_system_patrons = new ArrayList<>();
    }

    public Library_Management_System_Student(
        int StudentId,        String StudentName        ArrayList<Library_Management_System_Patron> library_management_system_patrons    ) {
        this.StudentId = StudentId;
        this.StudentName = StudentName;
        this.library_management_system_patrons = library_management_system_patrons;
    }

    public int getStudentid() {
        return StudentId;
    }

    public void setStudentid(int StudentId) {
        this.StudentId = StudentId;
    }
    public String getStudentname() {
        return StudentName;
    }

    public void setStudentname(String StudentName) {
        this.StudentName = StudentName;
    }

    public List<Library_Management_System_Patron> getLibrary_management_system_patrons() {
        return library_management_system_patrons;
    }

    public void addLibrary_management_system_patron(Library_management_system_patron library_management_system_patron) {
        this.library_management_system_patrons.add(library_management_system_patron);
    }

}