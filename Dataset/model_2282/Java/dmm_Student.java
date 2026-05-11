





import java.util.List;
import java.util.ArrayList;

public class dmm_Student extends Person {

    private int matriculationNumber;



    public dmm_Student(
        int matriculationNumber    ) {
        super(
        );
        this.matriculationNumber = matriculationNumber;
    }


    public int getMatriculationnumber() {
        return matriculationNumber;
    }

    public void setMatriculationnumber(int matriculationNumber) {
        this.matriculationNumber = matriculationNumber;
    }


}