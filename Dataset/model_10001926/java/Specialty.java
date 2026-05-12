





import java.util.List;
import java.util.ArrayList;

public class Specialty  {

    private String specialtyName;
    private int subjectCode;
    private int specialtyCode;
    private int id;



    public Specialty(
        String specialtyName,        int subjectCode,        int specialtyCode,        int id    ) {
        this.specialtyName = specialtyName;
        this.subjectCode = subjectCode;
        this.specialtyCode = specialtyCode;
        this.id = id;
    }


    public String getSpecialtyname() {
        return specialtyName;
    }

    public void setSpecialtyname(String specialtyName) {
        this.specialtyName = specialtyName;
    }
    public int getSubjectcode() {
        return subjectCode;
    }

    public void setSubjectcode(int subjectCode) {
        this.subjectCode = subjectCode;
    }
    public int getSpecialtycode() {
        return specialtyCode;
    }

    public void setSpecialtycode(int specialtyCode) {
        this.specialtyCode = specialtyCode;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}