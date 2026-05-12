





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private int administratorID;
    private String name;





    private AcademicRecords academicrecords;


    public Administrator(
        int administratorID,        String name    ) {
        this.administratorID = administratorID;
        this.name = name;
    }


    public int getAdministratorid() {
        return administratorID;
    }

    public void setAdministratorid(int administratorID) {
        this.administratorID = administratorID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public AcademicRecords getAcademicrecords() {
        return academicrecords;
    }

    public void setAcademicrecords(AcademicRecords academicrecords) {
        this.academicrecords = academicrecords;
    }

}