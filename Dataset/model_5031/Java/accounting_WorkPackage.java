




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class accounting_WorkPackage  {

    private float hours;
    private LocalDate date;
    private String task;
    private String comment;





    private accounting_Employee accounting_employee;




    private accounting_Project accounting_project;


    public accounting_WorkPackage(
        float hours,        LocalDate date,        String task,        String comment    ) {
        this.hours = hours;
        this.date = date;
        this.task = task;
        this.comment = comment;
    }


    public float getHours() {
        return hours;
    }

    public void setHours(float hours) {
        this.hours = hours;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public accounting_Employee getAccounting_employee() {
        return accounting_employee;
    }

    public void setAccounting_employee(accounting_Employee accounting_employee) {
        this.accounting_employee = accounting_employee;
    }
    public accounting_Project getAccounting_project() {
        return accounting_project;
    }

    public void setAccounting_project(accounting_Project accounting_project) {
        this.accounting_project = accounting_project;
    }

}