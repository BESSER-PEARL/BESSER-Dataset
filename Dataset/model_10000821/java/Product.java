




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Product  {

    private float price;
    private String title;
    private LocalDate creationDate;
    private boolean supportDiscount;



    public Product(
        float price,        String title,        LocalDate creationDate,        boolean supportDiscount    ) {
        this.price = price;
        this.title = title;
        this.creationDate = creationDate;
        this.supportDiscount = supportDiscount;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public boolean getSupportdiscount() {
        return supportDiscount;
    }

    public void setSupportdiscount(boolean supportDiscount) {
        this.supportDiscount = supportDiscount;
    }


}