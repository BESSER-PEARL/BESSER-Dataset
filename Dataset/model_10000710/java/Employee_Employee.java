





import java.util.List;
import java.util.ArrayList;

public class Employee_Employee  {

    private int dayByWeek;
    private None JobType;
    private String name;
    private None gender;
    private boolean isSuperUser;



    public Employee_Employee(
        int dayByWeek,        None JobType,        String name,        None gender,        boolean isSuperUser    ) {
        this.dayByWeek = dayByWeek;
        this.JobType = JobType;
        this.name = name;
        this.gender = gender;
        this.isSuperUser = isSuperUser;
    }


    public int getDaybyweek() {
        return dayByWeek;
    }

    public void setDaybyweek(int dayByWeek) {
        this.dayByWeek = dayByWeek;
    }
    public None getJobtype() {
        return JobType;
    }

    public void setJobtype(None JobType) {
        this.JobType = JobType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getGender() {
        return gender;
    }

    public void setGender(None gender) {
        this.gender = gender;
    }
    public boolean getIssuperuser() {
        return isSuperUser;
    }

    public void setIssuperuser(boolean isSuperUser) {
        this.isSuperUser = isSuperUser;
    }


}