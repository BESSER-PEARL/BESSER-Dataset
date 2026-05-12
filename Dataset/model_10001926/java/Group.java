





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private int id;
    private int groupNumber;
    private int educationalYear;
    private int specialtyCode;



    public Group(
        int id,        int groupNumber,        int educationalYear,        int specialtyCode    ) {
        this.id = id;
        this.groupNumber = groupNumber;
        this.educationalYear = educationalYear;
        this.specialtyCode = specialtyCode;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getGroupnumber() {
        return groupNumber;
    }

    public void setGroupnumber(int groupNumber) {
        this.groupNumber = groupNumber;
    }
    public int getEducationalyear() {
        return educationalYear;
    }

    public void setEducationalyear(int educationalYear) {
        this.educationalYear = educationalYear;
    }
    public int getSpecialtycode() {
        return specialtyCode;
    }

    public void setSpecialtycode(int specialtyCode) {
        this.specialtyCode = specialtyCode;
    }


}