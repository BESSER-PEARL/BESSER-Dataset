





import java.util.List;
import java.util.ArrayList;

public class ecvi_Animal  {

    private String age;
    private String breed;
    private String inspectionDate;
    private String sexDetail;
    private String sex;



    public ecvi_Animal(
        String age,        String breed,        String inspectionDate,        String sexDetail,        String sex    ) {
        this.age = age;
        this.breed = breed;
        this.inspectionDate = inspectionDate;
        this.sexDetail = sexDetail;
        this.sex = sex;
    }


    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public String getInspectiondate() {
        return inspectionDate;
    }

    public void setInspectiondate(String inspectionDate) {
        this.inspectionDate = inspectionDate;
    }
    public String getSexdetail() {
        return sexDetail;
    }

    public void setSexdetail(String sexDetail) {
        this.sexDetail = sexDetail;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }


}