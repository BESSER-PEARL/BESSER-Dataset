




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class timetrack_TimeEntry  {

    private String notes;
    private LocalDate till;
    private LocalDate duration;
    private LocalDate sync_date;
    private boolean factured;
    private LocalDate from_;
    private LocalDate day;





    private timetrack_Project timetrack_project;




    private timetrack_Library timetrack_library;




    private timetrack_User timetrack_user;


    public timetrack_TimeEntry(
        String notes,        LocalDate till,        LocalDate duration,        LocalDate sync_date,        boolean factured,        LocalDate from_,        LocalDate day    ) {
        this.notes = notes;
        this.till = till;
        this.duration = duration;
        this.sync_date = sync_date;
        this.factured = factured;
        this.from_ = from_;
        this.day = day;
    }


    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public LocalDate getTill() {
        return till;
    }

    public void setTill(LocalDate till) {
        this.till = till;
    }
    public LocalDate getDuration() {
        return duration;
    }

    public void setDuration(LocalDate duration) {
        this.duration = duration;
    }
    public LocalDate getSync_date() {
        return sync_date;
    }

    public void setSync_date(LocalDate sync_date) {
        this.sync_date = sync_date;
    }
    public boolean getFactured() {
        return factured;
    }

    public void setFactured(boolean factured) {
        this.factured = factured;
    }
    public LocalDate getFrom_() {
        return from_;
    }

    public void setFrom_(LocalDate from_) {
        this.from_ = from_;
    }
    public LocalDate getDay() {
        return day;
    }

    public void setDay(LocalDate day) {
        this.day = day;
    }

    public timetrack_Project getTimetrack_project() {
        return timetrack_project;
    }

    public void setTimetrack_project(timetrack_Project timetrack_project) {
        this.timetrack_project = timetrack_project;
    }
    public timetrack_Library getTimetrack_library() {
        return timetrack_library;
    }

    public void setTimetrack_library(timetrack_Library timetrack_library) {
        this.timetrack_library = timetrack_library;
    }
    public timetrack_User getTimetrack_user() {
        return timetrack_user;
    }

    public void setTimetrack_user(timetrack_User timetrack_user) {
        this.timetrack_user = timetrack_user;
    }

}