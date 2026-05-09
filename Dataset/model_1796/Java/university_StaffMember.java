





import java.util.List;
import java.util.ArrayList;

public class university_StaffMember extends NamedElement {

    private String staffMemberType;





    private List<university_Module> university_modules;




    private university_University university_university;




    private university_Department university_department;




    private university_Module university_module;


    public university_StaffMember(
        String staffMemberType    ) {
        super(
        );
        this.staffMemberType = staffMemberType;
        this.university_modules = new ArrayList<>();
    }

    public university_StaffMember(
        String staffMemberType        ArrayList<university_Module> university_modules    ) {
        this.staffMemberType = staffMemberType;
        this.university_modules = university_modules;
    }

    public String getStaffmembertype() {
        return staffMemberType;
    }

    public void setStaffmembertype(String staffMemberType) {
        this.staffMemberType = staffMemberType;
    }

    public List<university_Module> getUniversity_modules() {
        return university_modules;
    }

    public void addUniversity_module(University_module university_module) {
        this.university_modules.add(university_module);
    }
    public university_University getUniversity_university() {
        return university_university;
    }

    public void setUniversity_university(university_University university_university) {
        this.university_university = university_university;
    }
    public university_Department getUniversity_department() {
        return university_department;
    }

    public void setUniversity_department(university_Department university_department) {
        this.university_department = university_department;
    }
    public university_Module getUniversity_module() {
        return university_module;
    }

    public void setUniversity_module(university_Module university_module) {
        this.university_module = university_module;
    }

}