





import java.util.List;
import java.util.ArrayList;

public class programme_Programme  {

    private String code;
    private String programmeType;
    private String name;





    private programme_Department programme_department;


    public programme_Programme(
        String code,        String programmeType,        String name    ) {
        this.code = code;
        this.programmeType = programmeType;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getProgrammetype() {
        return programmeType;
    }

    public void setProgrammetype(String programmeType) {
        this.programmeType = programmeType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public programme_Department getProgramme_department() {
        return programme_department;
    }

    public void setProgramme_department(programme_Department programme_department) {
        this.programme_department = programme_department;
    }

}