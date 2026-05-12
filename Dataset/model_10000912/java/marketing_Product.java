




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class marketing_Product  {

    private String id;
    private None reviews;
    private None busId;
    private boolean active;
    private LocalDate expires;
    private None ccategory;
    private String name;
    private float price;
    private LocalDate created;



    public marketing_Product(
        String id,        None reviews,        None busId,        boolean active,        LocalDate expires,        None ccategory,        String name,        float price,        LocalDate created    ) {
        this.id = id;
        this.reviews = reviews;
        this.busId = busId;
        this.active = active;
        this.expires = expires;
        this.ccategory = ccategory;
        this.name = name;
        this.price = price;
        this.created = created;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getReviews() {
        return reviews;
    }

    public void setReviews(None reviews) {
        this.reviews = reviews;
    }
    public None getBusid() {
        return busId;
    }

    public void setBusid(None busId) {
        this.busId = busId;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public LocalDate getExpires() {
        return expires;
    }

    public void setExpires(LocalDate expires) {
        this.expires = expires;
    }
    public None getCcategory() {
        return ccategory;
    }

    public void setCcategory(None ccategory) {
        this.ccategory = ccategory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }


}