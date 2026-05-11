





import java.util.List;
import java.util.ArrayList;

public class study_Programme  {

    private String name;
    private String programmeCode;





    private study_Department study_department;


    public study_Programme(
        String name,        String programmeCode    ) {
        this.name = name;
        this.programmeCode = programmeCode;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProgrammecode() {
        return programmeCode;
    }

    public void setProgrammecode(String programmeCode) {
        this.programmeCode = programmeCode;
    }

    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }

}