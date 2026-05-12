





import java.util.List;
import java.util.ArrayList;

public class Signs  {

    private String name;
    private int ID;





    private Diagnosis diagnosis;


    public Signs(
        String name,        int ID    ) {
        this.name = name;
        this.ID = ID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Diagnosis getDiagnosis() {
        return diagnosis;
    }

    public void setDiagnosis(Diagnosis diagnosis) {
        this.diagnosis = diagnosis;
    }

}