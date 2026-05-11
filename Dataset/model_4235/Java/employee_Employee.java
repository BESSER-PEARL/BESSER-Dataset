





import java.util.List;
import java.util.ArrayList;

public class employee_Employee  {

    private String name;
    private String age;
    private String hireDate;
    private String salary;





    private employee_Department employee_department;


    public employee_Employee(
        String name,        String age,        String hireDate,        String salary    ) {
        this.name = name;
        this.age = age;
        this.hireDate = hireDate;
        this.salary = salary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getHiredate() {
        return hireDate;
    }

    public void setHiredate(String hireDate) {
        this.hireDate = hireDate;
    }
    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }

    public employee_Department getEmployee_department() {
        return employee_department;
    }

    public void setEmployee_department(employee_Department employee_department) {
        this.employee_department = employee_department;
    }

}