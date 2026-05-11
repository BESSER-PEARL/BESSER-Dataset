





import java.util.List;
import java.util.ArrayList;

public class ra_Course  {

    private String code;
    private String name;





    private ra_Semester ra_semester;




    private ra_Department ra_department;


    public ra_Course(
        String code,        String name    ) {
        this.code = code;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ra_Semester getRa_semester() {
        return ra_semester;
    }

    public void setRa_semester(ra_Semester ra_semester) {
        this.ra_semester = ra_semester;
    }
    public ra_Department getRa_department() {
        return ra_department;
    }

    public void setRa_department(ra_Department ra_department) {
        this.ra_department = ra_department;
    }

}