





import java.util.List;
import java.util.ArrayList;

public class StudyProgrammes_Specialization  {

    private int startSemester;
    private int lengthInSemesters;
    private String name;





    private StudyProgrammes_Programme studyprogrammes_programme;


    public StudyProgrammes_Specialization(
        int startSemester,        int lengthInSemesters,        String name    ) {
        this.startSemester = startSemester;
        this.lengthInSemesters = lengthInSemesters;
        this.name = name;
    }


    public int getStartsemester() {
        return startSemester;
    }

    public void setStartsemester(int startSemester) {
        this.startSemester = startSemester;
    }
    public int getLengthinsemesters() {
        return lengthInSemesters;
    }

    public void setLengthinsemesters(int lengthInSemesters) {
        this.lengthInSemesters = lengthInSemesters;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StudyProgrammes_Programme getStudyprogrammes_programme() {
        return studyprogrammes_programme;
    }

    public void setStudyprogrammes_programme(StudyProgrammes_Programme studyprogrammes_programme) {
        this.studyprogrammes_programme = studyprogrammes_programme;
    }

}