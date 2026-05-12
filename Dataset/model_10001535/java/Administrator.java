





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String name;
    private int administratorID;





    private AcademicRecords academicrecords;


    public Administrator(
        String name,        int administratorID    ) {
        this.name = name;
        this.administratorID = administratorID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAdministratorid() {
        return administratorID;
    }

    public void setAdministratorid(int administratorID) {
        this.administratorID = administratorID;
    }

    public AcademicRecords getAcademicrecords() {
        return academicrecords;
    }

    public void setAcademicrecords(AcademicRecords academicrecords) {
        this.academicrecords = academicrecords;
    }

}