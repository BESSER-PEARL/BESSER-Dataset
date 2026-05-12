




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Reviews  {

    private String text;
    private int user_id;
    private int business_id;
    private LocalDate date;
    private int ID;
    private int rating;



    public Reviews(
        String text,        int user_id,        int business_id,        LocalDate date,        int ID,        int rating    ) {
        this.text = text;
        this.user_id = user_id;
        this.business_id = business_id;
        this.date = date;
        this.ID = ID;
        this.rating = rating;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getBusiness_id() {
        return business_id;
    }

    public void setBusiness_id(int business_id) {
        this.business_id = business_id;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }


}