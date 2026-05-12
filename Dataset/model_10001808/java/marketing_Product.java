




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class marketing_Product  {

    private String name;
    private None busId;
    private String id;
    private None reviews;
    private None ccategory;
    private boolean active;
    private LocalDate created;
    private LocalDate expires;
    private float price;



    public marketing_Product(
        String name,        None busId,        String id,        None reviews,        None ccategory,        boolean active,        LocalDate created,        LocalDate expires,        float price    ) {
        this.name = name;
        this.busId = busId;
        this.id = id;
        this.reviews = reviews;
        this.ccategory = ccategory;
        this.active = active;
        this.created = created;
        this.expires = expires;
        this.price = price;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getBusid() {
        return busId;
    }

    public void setBusid(None busId) {
        this.busId = busId;
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
    public None getCcategory() {
        return ccategory;
    }

    public void setCcategory(None ccategory) {
        this.ccategory = ccategory;
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
    public LocalDate getExpires() {
        return expires;
    }

    public void setExpires(LocalDate expires) {
        this.expires = expires;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }


}