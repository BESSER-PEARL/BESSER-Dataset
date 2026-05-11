





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_Semester  {

    private String season;
    private int year;





    private studyProgramStructure_Specialization studyprogramstructure_specialization;




    private studyProgramStructure_Program studyprogramstructure_program;




    private studyProgramStructure_Specialization studyprogramstructure_specialization;




    private studyProgramStructure_Program studyprogramstructure_program;


    public studyProgramStructure_Semester(
        String season,        int year    ) {
        this.season = season;
        this.year = year;
    }


    public String getSeason() {
        return season;
    }

    public void setSeason(String season) {
        this.season = season;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public studyProgramStructure_Specialization getStudyprogramstructure_specialization() {
        return studyprogramstructure_specialization;
    }

    public void setStudyprogramstructure_specialization(studyProgramStructure_Specialization studyprogramstructure_specialization) {
        this.studyprogramstructure_specialization = studyprogramstructure_specialization;
    }
    public studyProgramStructure_Program getStudyprogramstructure_program() {
        return studyprogramstructure_program;
    }

    public void setStudyprogramstructure_program(studyProgramStructure_Program studyprogramstructure_program) {
        this.studyprogramstructure_program = studyprogramstructure_program;
    }
    public studyProgramStructure_Specialization getStudyprogramstructure_specialization() {
        return studyprogramstructure_specialization;
    }

    public void setStudyprogramstructure_specialization(studyProgramStructure_Specialization studyprogramstructure_specialization) {
        this.studyprogramstructure_specialization = studyprogramstructure_specialization;
    }
    public studyProgramStructure_Program getStudyprogramstructure_program() {
        return studyprogramstructure_program;
    }

    public void setStudyprogramstructure_program(studyProgramStructure_Program studyprogramstructure_program) {
        this.studyprogramstructure_program = studyprogramstructure_program;
    }

}