





import java.util.List;
import java.util.ArrayList;

public class Symptoms  {

    private int ID;
    private String name;





    private Diagnosis diagnosis;


    public Symptoms(
        int ID,        String name    ) {
        this.ID = ID;
        this.name = name;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Diagnosis getDiagnosis() {
        return diagnosis;
    }

    public void setDiagnosis(Diagnosis diagnosis) {
        this.diagnosis = diagnosis;
    }

}