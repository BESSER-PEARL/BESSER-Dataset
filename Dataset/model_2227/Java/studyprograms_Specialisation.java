





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Specialisation  {

    private int startSemester;
    private String name;





    private studyprograms_Programme studyprograms_programme;




    private studyprograms_Specialisation studyprograms_specialisation;


    public studyprograms_Specialisation(
        int startSemester,        String name    ) {
        this.startSemester = startSemester;
        this.name = name;
    }


    public int getStartsemester() {
        return startSemester;
    }

    public void setStartsemester(int startSemester) {
        this.startSemester = startSemester;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyprograms_Programme getStudyprograms_programme() {
        return studyprograms_programme;
    }

    public void setStudyprograms_programme(studyprograms_Programme studyprograms_programme) {
        this.studyprograms_programme = studyprograms_programme;
    }
    public studyprograms_Specialisation getStudyprograms_specialisation() {
        return studyprograms_specialisation;
    }

    public void setStudyprograms_specialisation(studyprograms_Specialisation studyprograms_specialisation) {
        this.studyprograms_specialisation = studyprograms_specialisation;
    }

}