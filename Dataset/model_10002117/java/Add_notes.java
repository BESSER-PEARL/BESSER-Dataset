





import java.util.List;
import java.util.ArrayList;

public class Add_notes  {

    private String Notes_taken;
    private int Student_ID;
    private String Course_Name;





    private Home_page home_page;


    public Add_notes(
        String Notes_taken,        int Student_ID,        String Course_Name    ) {
        this.Notes_taken = Notes_taken;
        this.Student_ID = Student_ID;
        this.Course_Name = Course_Name;
    }


    public String getNotes_taken() {
        return Notes_taken;
    }

    public void setNotes_taken(String Notes_taken) {
        this.Notes_taken = Notes_taken;
    }
    public int getStudent_id() {
        return Student_ID;
    }

    public void setStudent_id(int Student_ID) {
        this.Student_ID = Student_ID;
    }
    public String getCourse_name() {
        return Course_Name;
    }

    public void setCourse_name(String Course_Name) {
        this.Course_Name = Course_Name;
    }

    public Home_page getHome_page() {
        return home_page;
    }

    public void setHome_page(Home_page home_page) {
        this.home_page = home_page;
    }

}