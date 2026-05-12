





import java.util.List;
import java.util.ArrayList;

public class Instructions  {

    private int ID;
    private String descriptions;
    private String name;





    private Diagnosis diagnosis;


    public Instructions(
        int ID,        String descriptions,        String name    ) {
        this.ID = ID;
        this.descriptions = descriptions;
        this.name = name;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getDescriptions() {
        return descriptions;
    }

    public void setDescriptions(String descriptions) {
        this.descriptions = descriptions;
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