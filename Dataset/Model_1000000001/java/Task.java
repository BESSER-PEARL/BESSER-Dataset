




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class Task  {

    private LocalDateTime due_date;
    private LocalDateTime created_at;
    private String title;
    private int id;
    private LocalDateTime completed_at;
    private String description;
    private boolean is_completed;





    private Opportunity opportunity;




    private User user;




    private Contact contact;


    public Task(
        LocalDateTime due_date,        LocalDateTime created_at,        String title,        int id,        LocalDateTime completed_at,        String description,        boolean is_completed    ) {
        this.due_date = due_date;
        this.created_at = created_at;
        this.title = title;
        this.id = id;
        this.completed_at = completed_at;
        this.description = description;
        this.is_completed = is_completed;
    }


    public LocalDateTime getDue_date() {
        return due_date;
    }

    public void setDue_date(LocalDateTime due_date) {
        this.due_date = due_date;
    }
    public LocalDateTime getCreated_at() {
        return created_at;
    }

    public void setCreated_at(LocalDateTime created_at) {
        this.created_at = created_at;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDateTime getCompleted_at() {
        return completed_at;
    }

    public void setCompleted_at(LocalDateTime completed_at) {
        this.completed_at = completed_at;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getIs_completed() {
        return is_completed;
    }

    public void setIs_completed(boolean is_completed) {
        this.is_completed = is_completed;
    }

    public Opportunity getOpportunity() {
        return opportunity;
    }

    public void setOpportunity(Opportunity opportunity) {
        this.opportunity = opportunity;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Contact getContact() {
        return contact;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }

}