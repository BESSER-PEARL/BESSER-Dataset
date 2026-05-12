





import java.util.List;
import java.util.ArrayList;

public class Library_Management_System_Student  {

    private String StudentName;
    private int StudentId;





    private List<Library_Management_System_Patron> library_management_system_patrons;


    public Library_Management_System_Student(
        String StudentName,        int StudentId    ) {
        this.StudentName = StudentName;
        this.StudentId = StudentId;
        this.library_management_system_patrons = new ArrayList<>();
    }

    public Library_Management_System_Student(
        String StudentName,        int StudentId        ArrayList<Library_Management_System_Patron> library_management_system_patrons    ) {
        this.StudentName = StudentName;
        this.StudentId = StudentId;
        this.library_management_system_patrons = library_management_system_patrons;
    }

    public String getStudentname() {
        return StudentName;
    }

    public void setStudentname(String StudentName) {
        this.StudentName = StudentName;
    }
    public int getStudentid() {
        return StudentId;
    }

    public void setStudentid(int StudentId) {
        this.StudentId = StudentId;
    }

    public List<Library_Management_System_Patron> getLibrary_management_system_patrons() {
        return library_management_system_patrons;
    }

    public void addLibrary_management_system_patron(Library_management_system_patron library_management_system_patron) {
        this.library_management_system_patrons.add(library_management_system_patron);
    }

}