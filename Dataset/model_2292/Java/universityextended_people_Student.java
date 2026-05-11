





import java.util.List;
import java.util.ArrayList;

public class universityextended_people_Student extends Person {

    private String matriculationnumber;



    public universityextended_people_Student(
        String matriculationnumber    ) {
        super(
        );
        this.matriculationnumber = matriculationnumber;
    }


    public String getMatriculationnumber() {
        return matriculationnumber;
    }

    public void setMatriculationnumber(String matriculationnumber) {
        this.matriculationnumber = matriculationnumber;
    }


}