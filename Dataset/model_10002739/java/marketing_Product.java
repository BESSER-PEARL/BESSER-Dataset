




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class marketing_Product  {

    private String name;
    private None reviews;
    private boolean active;
    private LocalDate created;
    private None ccategory;
    private LocalDate expires;
    private String id;
    private float price;
    private None busId;



    public marketing_Product(
        String name,        None reviews,        boolean active,        LocalDate created,        None ccategory,        LocalDate expires,        String id,        float price,        None busId    ) {
        this.name = name;
        this.reviews = reviews;
        this.active = active;
        this.created = created;
        this.ccategory = ccategory;
        this.expires = expires;
        this.id = id;
        this.price = price;
        this.busId = busId;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getReviews() {
        return reviews;
    }

    public void setReviews(None reviews) {
        this.reviews = reviews;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public None getCcategory() {
        return ccategory;
    }

    public void setCcategory(None ccategory) {
        this.ccategory = ccategory;
    }
    public LocalDate getExpires() {
        return expires;
    }

    public void setExpires(LocalDate expires) {
        this.expires = expires;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public None getBusid() {
        return busId;
    }

    public void setBusid(None busId) {
        this.busId = busId;
    }


}