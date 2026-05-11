




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class restapp_model_ProductsCard  {

    private int id;
    private LocalDate date;





    private User user;


    public restapp_model_ProductsCard(
        int id,        LocalDate date    ) {
        this.id = id;
        this.date = date;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}