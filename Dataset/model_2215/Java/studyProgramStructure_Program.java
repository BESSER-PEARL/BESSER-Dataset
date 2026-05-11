





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_Program  {

    private String code;
    private int numOfYears;
    private String name;
    private int numOfSemestersForBaseSpecialization;



    public studyProgramStructure_Program(
        String code,        int numOfYears,        String name,        int numOfSemestersForBaseSpecialization    ) {
        this.code = code;
        this.numOfYears = numOfYears;
        this.name = name;
        this.numOfSemestersForBaseSpecialization = numOfSemestersForBaseSpecialization;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public int getNumofyears() {
        return numOfYears;
    }

    public void setNumofyears(int numOfYears) {
        this.numOfYears = numOfYears;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumofsemestersforbasespecialization() {
        return numOfSemestersForBaseSpecialization;
    }

    public void setNumofsemestersforbasespecialization(int numOfSemestersForBaseSpecialization) {
        this.numOfSemestersForBaseSpecialization = numOfSemestersForBaseSpecialization;
    }


}