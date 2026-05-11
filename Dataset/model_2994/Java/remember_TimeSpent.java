




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class remember_TimeSpent  {

    private LocalDate date;
    private String timeSpentId;
    private String comment;
    private boolean invoiced;
    private int minutes;





    private remember_Task remember_task;




    private remember_Task remember_task;


    public remember_TimeSpent(
        LocalDate date,        String timeSpentId,        String comment,        boolean invoiced,        int minutes    ) {
        this.date = date;
        this.timeSpentId = timeSpentId;
        this.comment = comment;
        this.invoiced = invoiced;
        this.minutes = minutes;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getTimespentid() {
        return timeSpentId;
    }

    public void setTimespentid(String timeSpentId) {
        this.timeSpentId = timeSpentId;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public boolean getInvoiced() {
        return invoiced;
    }

    public void setInvoiced(boolean invoiced) {
        this.invoiced = invoiced;
    }
    public int getMinutes() {
        return minutes;
    }

    public void setMinutes(int minutes) {
        this.minutes = minutes;
    }

    public remember_Task getRemember_task() {
        return remember_task;
    }

    public void setRemember_task(remember_Task remember_task) {
        this.remember_task = remember_task;
    }
    public remember_Task getRemember_task() {
        return remember_task;
    }

    public void setRemember_task(remember_Task remember_task) {
        this.remember_task = remember_task;
    }

}