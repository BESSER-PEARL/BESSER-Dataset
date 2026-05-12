





import java.util.List;
import java.util.ArrayList;

public class Admin_  {

    private String Password;
    private String ArrayList_member_;
    private String ArryList_Employee;





    private Employee employee;




    private member member;


    public Admin_(
        String Password,        String ArrayList_member_,        String ArryList_Employee    ) {
        this.Password = Password;
        this.ArrayList_member_ = ArrayList_member_;
        this.ArryList_Employee = ArryList_Employee;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getArraylist_member_() {
        return ArrayList_member_;
    }

    public void setArraylist_member_(String ArrayList_member_) {
        this.ArrayList_member_ = ArrayList_member_;
    }
    public String getArrylist_employee() {
        return ArryList_Employee;
    }

    public void setArrylist_employee(String ArryList_Employee) {
        this.ArryList_Employee = ArryList_Employee;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }
    public member getMember() {
        return member;
    }

    public void setMember(member member) {
        this.member = member;
    }

}