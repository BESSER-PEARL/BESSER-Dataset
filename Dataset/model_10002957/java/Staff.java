





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private float salary_scale;
    private None position;
    private int num;
    private None employment_contract;
    private None qualification;
    private int nin;
    private None work_experience;
    private float current_salary;



    public Staff(
        float salary_scale,        None position,        int num,        None employment_contract,        None qualification,        int nin,        None work_experience,        float current_salary    ) {
        this.salary_scale = salary_scale;
        this.position = position;
        this.num = num;
        this.employment_contract = employment_contract;
        this.qualification = qualification;
        this.nin = nin;
        this.work_experience = work_experience;
        this.current_salary = current_salary;
    }


    public float getSalary_scale() {
        return salary_scale;
    }

    public void setSalary_scale(float salary_scale) {
        this.salary_scale = salary_scale;
    }
    public None getPosition() {
        return position;
    }

    public void setPosition(None position) {
        this.position = position;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public None getEmployment_contract() {
        return employment_contract;
    }

    public void setEmployment_contract(None employment_contract) {
        this.employment_contract = employment_contract;
    }
    public None getQualification() {
        return qualification;
    }

    public void setQualification(None qualification) {
        this.qualification = qualification;
    }
    public int getNin() {
        return nin;
    }

    public void setNin(int nin) {
        this.nin = nin;
    }
    public None getWork_experience() {
        return work_experience;
    }

    public void setWork_experience(None work_experience) {
        this.work_experience = work_experience;
    }
    public float getCurrent_salary() {
        return current_salary;
    }

    public void setCurrent_salary(float current_salary) {
        this.current_salary = current_salary;
    }


}