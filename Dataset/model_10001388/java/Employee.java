





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String emp_email;
    private String emp_name;
    private int emp_id;



    public Employee(
        String emp_email,        String emp_name,        int emp_id    ) {
        this.emp_email = emp_email;
        this.emp_name = emp_name;
        this.emp_id = emp_id;
    }


    public String getEmp_email() {
        return emp_email;
    }

    public void setEmp_email(String emp_email) {
        this.emp_email = emp_email;
    }
    public String getEmp_name() {
        return emp_name;
    }

    public void setEmp_name(String emp_name) {
        this.emp_name = emp_name;
    }
    public int getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(int emp_id) {
        this.emp_id = emp_id;
    }


}