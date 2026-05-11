





import java.util.List;
import java.util.ArrayList;

public class tdt4250_StudyProgram  {

    private String name;
    private int number_of_semesters;



    public tdt4250_StudyProgram(
        String name,        int number_of_semesters    ) {
        this.name = name;
        this.number_of_semesters = number_of_semesters;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumber_of_semesters() {
        return number_of_semesters;
    }

    public void setNumber_of_semesters(int number_of_semesters) {
        this.number_of_semesters = number_of_semesters;
    }


}