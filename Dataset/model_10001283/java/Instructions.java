





import java.util.List;
import java.util.ArrayList;

public class Instructions  {

    private String name;
    private String descriptions;
    private int ID;





    private Diagnosis diagnosis;


    public Instructions(
        String name,        String descriptions,        int ID    ) {
        this.name = name;
        this.descriptions = descriptions;
        this.ID = ID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescriptions() {
        return descriptions;
    }

    public void setDescriptions(String descriptions) {
        this.descriptions = descriptions;
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