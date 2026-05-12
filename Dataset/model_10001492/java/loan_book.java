




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class loan_book  {

    private LocalDate loan_date;
    private LocalDate returned_date;
    private int cost;
    private LocalDate due_date;
    private int id;





    private user user;


    public loan_book(
        LocalDate loan_date,        LocalDate returned_date,        int cost,        LocalDate due_date,        int id    ) {
        this.loan_date = loan_date;
        this.returned_date = returned_date;
        this.cost = cost;
        this.due_date = due_date;
        this.id = id;
    }


    public LocalDate getLoan_date() {
        return loan_date;
    }

    public void setLoan_date(LocalDate loan_date) {
        this.loan_date = loan_date;
    }
    public LocalDate getReturned_date() {
        return returned_date;
    }

    public void setReturned_date(LocalDate returned_date) {
        this.returned_date = returned_date;
    }
    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }
    public LocalDate getDue_date() {
        return due_date;
    }

    public void setDue_date(LocalDate due_date) {
        this.due_date = due_date;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}