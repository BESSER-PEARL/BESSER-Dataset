





import java.util.List;
import java.util.ArrayList;

public class tdt4250case_Person  {

    private String username;
    private String name;





    private tdt4250case_Department tdt4250case_department;




    private tdt4250case_CourseRole tdt4250case_courserole;




    private List<tdt4250case_CourseRole> tdt4250case_courseroles;


    public tdt4250case_Person(
        String username,        String name    ) {
        this.username = username;
        this.name = name;
        this.tdt4250case_courseroles = new ArrayList<>();
    }

    public tdt4250case_Person(
        String username,        String name        ArrayList<tdt4250case_CourseRole> tdt4250case_courseroles    ) {
        this.username = username;
        this.name = name;
        this.tdt4250case_courseroles = tdt4250case_courseroles;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tdt4250case_Department getTdt4250case_department() {
        return tdt4250case_department;
    }

    public void setTdt4250case_department(tdt4250case_Department tdt4250case_department) {
        this.tdt4250case_department = tdt4250case_department;
    }
    public tdt4250case_CourseRole getTdt4250case_courserole() {
        return tdt4250case_courserole;
    }

    public void setTdt4250case_courserole(tdt4250case_CourseRole tdt4250case_courserole) {
        this.tdt4250case_courserole = tdt4250case_courserole;
    }
    public List<tdt4250case_CourseRole> getTdt4250case_courseroles() {
        return tdt4250case_courseroles;
    }

    public void addTdt4250case_courserole(Tdt4250case_courserole tdt4250case_courserole) {
        this.tdt4250case_courseroles.add(tdt4250case_courserole);
    }

}