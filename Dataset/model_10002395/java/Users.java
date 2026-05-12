




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Users  {

    private int review_count;
    private int ID;
    private String name;
    private LocalDate date_joined;
    private int average_star;



    public Users(
        int review_count,        int ID,        String name,        LocalDate date_joined,        int average_star    ) {
        this.review_count = review_count;
        this.ID = ID;
        this.name = name;
        this.date_joined = date_joined;
        this.average_star = average_star;
    }


    public int getReview_count() {
        return review_count;
    }

    public void setReview_count(int review_count) {
        this.review_count = review_count;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getDate_joined() {
        return date_joined;
    }

    public void setDate_joined(LocalDate date_joined) {
        this.date_joined = date_joined;
    }
    public int getAverage_star() {
        return average_star;
    }

    public void setAverage_star(int average_star) {
        this.average_star = average_star;
    }


}