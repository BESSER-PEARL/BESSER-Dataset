




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class restapp_model_Purchase  {

    private LocalDate date;
    private float totalValue;
    private float totalWithDiscount;
    private int discount;
    private int id;





    private User user;


    public restapp_model_Purchase(
        LocalDate date,        float totalValue,        float totalWithDiscount,        int discount,        int id    ) {
        this.date = date;
        this.totalValue = totalValue;
        this.totalWithDiscount = totalWithDiscount;
        this.discount = discount;
        this.id = id;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public float getTotalvalue() {
        return totalValue;
    }

    public void setTotalvalue(float totalValue) {
        this.totalValue = totalValue;
    }
    public float getTotalwithdiscount() {
        return totalWithDiscount;
    }

    public void setTotalwithdiscount(float totalWithDiscount) {
        this.totalWithDiscount = totalWithDiscount;
    }
    public int getDiscount() {
        return discount;
    }

    public void setDiscount(int discount) {
        this.discount = discount;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}