





import java.util.List;
import java.util.ArrayList;

public class oving1APD_StudyProgram  {

    private String name;
    private String shortName;





    private oving1APD_Semester oving1apd_semester;




    private List<oving1APD_Specialization> oving1apd_specializations;




    private oving1APD_Specialization oving1apd_specialization;




    private oving1APD_Semester oving1apd_semester;




    private oving1APD_Department oving1apd_department;




    private oving1APD_Department oving1apd_department;


    public oving1APD_StudyProgram(
        String name,        String shortName    ) {
        this.name = name;
        this.shortName = shortName;
        this.oving1apd_specializations = new ArrayList<>();
    }

    public oving1APD_StudyProgram(
        String name,        String shortName        ArrayList<oving1APD_Specialization> oving1apd_specializations    ) {
        this.name = name;
        this.shortName = shortName;
        this.oving1apd_specializations = oving1apd_specializations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }

    public oving1APD_Semester getOving1apd_semester() {
        return oving1apd_semester;
    }

    public void setOving1apd_semester(oving1APD_Semester oving1apd_semester) {
        this.oving1apd_semester = oving1apd_semester;
    }
    public List<oving1APD_Specialization> getOving1apd_specializations() {
        return oving1apd_specializations;
    }

    public void addOving1apd_specialization(Oving1apd_specialization oving1apd_specialization) {
        this.oving1apd_specializations.add(oving1apd_specialization);
    }
    public oving1APD_Specialization getOving1apd_specialization() {
        return oving1apd_specialization;
    }

    public void setOving1apd_specialization(oving1APD_Specialization oving1apd_specialization) {
        this.oving1apd_specialization = oving1apd_specialization;
    }
    public oving1APD_Semester getOving1apd_semester() {
        return oving1apd_semester;
    }

    public void setOving1apd_semester(oving1APD_Semester oving1apd_semester) {
        this.oving1apd_semester = oving1apd_semester;
    }
    public oving1APD_Department getOving1apd_department() {
        return oving1apd_department;
    }

    public void setOving1apd_department(oving1APD_Department oving1apd_department) {
        this.oving1apd_department = oving1apd_department;
    }
    public oving1APD_Department getOving1apd_department() {
        return oving1apd_department;
    }

    public void setOving1apd_department(oving1APD_Department oving1apd_department) {
        this.oving1apd_department = oving1apd_department;
    }

}