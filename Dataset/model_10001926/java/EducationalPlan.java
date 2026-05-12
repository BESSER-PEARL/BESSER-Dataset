





import java.util.List;
import java.util.ArrayList;

public class EducationalPlan  {

    private int individualIdentificationCode;
    private int id;
    private int subjectCode;



    public EducationalPlan(
        int individualIdentificationCode,        int id,        int subjectCode    ) {
        this.individualIdentificationCode = individualIdentificationCode;
        this.id = id;
        this.subjectCode = subjectCode;
    }


    public int getIndividualidentificationcode() {
        return individualIdentificationCode;
    }

    public void setIndividualidentificationcode(int individualIdentificationCode) {
        this.individualIdentificationCode = individualIdentificationCode;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getSubjectcode() {
        return subjectCode;
    }

    public void setSubjectcode(int subjectCode) {
        this.subjectCode = subjectCode;
    }


}