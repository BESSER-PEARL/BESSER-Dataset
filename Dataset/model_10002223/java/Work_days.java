





import java.util.List;
import java.util.ArrayList;

public class Work_days  {

    private int Days_Attended;
    private int _No__of_working_days_;





    private List<Salary> salarys;




    private List<DaysAttended> daysattendeds;


    public Work_days(
        int Days_Attended,        int _No__of_working_days_    ) {
        this.Days_Attended = Days_Attended;
        this._No__of_working_days_ = _No__of_working_days_;
        this.salarys = new ArrayList<>();
        this.daysattendeds = new ArrayList<>();
    }

    public Work_days(
        int Days_Attended,        int _No__of_working_days_        ArrayList<Salary> salarys,        ArrayList<DaysAttended> daysattendeds    ) {
        this.Days_Attended = Days_Attended;
        this._No__of_working_days_ = _No__of_working_days_;
        this.salarys = salarys;
        this.daysattendeds = daysattendeds;
    }

    public int getDays_attended() {
        return Days_Attended;
    }

    public void setDays_attended(int Days_Attended) {
        this.Days_Attended = Days_Attended;
    }
    public int get_no__of_working_days_() {
        return _No__of_working_days_;
    }

    public void set_no__of_working_days_(int _No__of_working_days_) {
        this._No__of_working_days_ = _No__of_working_days_;
    }

    public List<Salary> getSalarys() {
        return salarys;
    }

    public void addSalary(Salary salary) {
        this.salarys.add(salary);
    }
    public List<DaysAttended> getDaysattendeds() {
        return daysattendeds;
    }

    public void addDaysattended(Daysattended daysattended) {
        this.daysattendeds.add(daysattended);
    }

}