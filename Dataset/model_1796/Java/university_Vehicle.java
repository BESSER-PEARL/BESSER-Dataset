





import java.util.List;
import java.util.ArrayList;

public class university_Vehicle  {

    private String registrationNumber;





    private university_Student university_student;




    private university_StaffMember university_staffmember;




    private university_Library university_library;


    public university_Vehicle(
        String registrationNumber    ) {
        this.registrationNumber = registrationNumber;
    }


    public String getRegistrationnumber() {
        return registrationNumber;
    }

    public void setRegistrationnumber(String registrationNumber) {
        this.registrationNumber = registrationNumber;
    }

    public university_Student getUniversity_student() {
        return university_student;
    }

    public void setUniversity_student(university_Student university_student) {
        this.university_student = university_student;
    }
    public university_StaffMember getUniversity_staffmember() {
        return university_staffmember;
    }

    public void setUniversity_staffmember(university_StaffMember university_staffmember) {
        this.university_staffmember = university_staffmember;
    }
    public university_Library getUniversity_library() {
        return university_library;
    }

    public void setUniversity_library(university_Library university_library) {
        this.university_library = university_library;
    }

}