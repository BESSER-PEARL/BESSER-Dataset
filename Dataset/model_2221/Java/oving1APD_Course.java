





import java.util.List;
import java.util.ArrayList;

public class oving1APD_Course  {

    private String name;
    private float credit;
    private int level;
    private String code;





    private List<oving1APD_Semester> oving1apd_semesters;




    private oving1APD_Semester oving1apd_semester;




    private oving1APD_Specialization oving1apd_specialization;




    private oving1APD_Department oving1apd_department;




    private oving1APD_Specialization oving1apd_specialization;


    public oving1APD_Course(
        String name,        float credit,        int level,        String code    ) {
        this.name = name;
        this.credit = credit;
        this.level = level;
        this.code = code;
        this.oving1apd_semesters = new ArrayList<>();
    }

    public oving1APD_Course(
        String name,        float credit,        int level,        String code        ArrayList<oving1APD_Semester> oving1apd_semesters    ) {
        this.name = name;
        this.credit = credit;
        this.level = level;
        this.code = code;
        this.oving1apd_semesters = oving1apd_semesters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public List<oving1APD_Semester> getOving1apd_semesters() {
        return oving1apd_semesters;
    }

    public void addOving1apd_semester(Oving1apd_semester oving1apd_semester) {
        this.oving1apd_semesters.add(oving1apd_semester);
    }
    public oving1APD_Semester getOving1apd_semester() {
        return oving1apd_semester;
    }

    public void setOving1apd_semester(oving1APD_Semester oving1apd_semester) {
        this.oving1apd_semester = oving1apd_semester;
    }
    public oving1APD_Specialization getOving1apd_specialization() {
        return oving1apd_specialization;
    }

    public void setOving1apd_specialization(oving1APD_Specialization oving1apd_specialization) {
        this.oving1apd_specialization = oving1apd_specialization;
    }
    public oving1APD_Department getOving1apd_department() {
        return oving1apd_department;
    }

    public void setOving1apd_department(oving1APD_Department oving1apd_department) {
        this.oving1apd_department = oving1apd_department;
    }
    public oving1APD_Specialization getOving1apd_specialization() {
        return oving1apd_specialization;
    }

    public void setOving1apd_specialization(oving1APD_Specialization oving1apd_specialization) {
        this.oving1apd_specialization = oving1apd_specialization;
    }

}