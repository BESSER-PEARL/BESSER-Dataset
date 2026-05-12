





import java.util.List;
import java.util.ArrayList;

public class Librarian  {

    private int LibID;
    private String Department;



    public Librarian(
        int LibID,        String Department    ) {
        this.LibID = LibID;
        this.Department = Department;
    }


    public int getLibid() {
        return LibID;
    }

    public void setLibid(int LibID) {
        this.LibID = LibID;
    }
    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }


}