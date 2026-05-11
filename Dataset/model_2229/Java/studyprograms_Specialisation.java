





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Specialisation  {

    private String name;
    private int startSemester;





    private studyprograms_Programme studyprograms_programme;


    public studyprograms_Specialisation(
        String name,        int startSemester    ) {
        this.name = name;
        this.startSemester = startSemester;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getStartsemester() {
        return startSemester;
    }

    public void setStartsemester(int startSemester) {
        this.startSemester = startSemester;
    }

    public studyprograms_Programme getStudyprograms_programme() {
        return studyprograms_programme;
    }

    public void setStudyprograms_programme(studyprograms_Programme studyprograms_programme) {
        this.studyprograms_programme = studyprograms_programme;
    }

}