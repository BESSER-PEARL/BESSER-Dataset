




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class marketing_Product  {

    private String id;
    private None ccategory;
    private None reviews;
    private LocalDate created;
    private boolean active;
    private float price;
    private None busId;
    private String name;
    private LocalDate expires;



    public marketing_Product(
        String id,        None ccategory,        None reviews,        LocalDate created,        boolean active,        float price,        None busId,        String name,        LocalDate expires    ) {
        this.id = id;
        this.ccategory = ccategory;
        this.reviews = reviews;
        this.created = created;
        this.active = active;
        this.price = price;
        this.busId = busId;
        this.name = name;
        this.expires = expires;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getCcategory() {
        return ccategory;
    }

    public void setCcategory(None ccategory) {
        this.ccategory = ccategory;
    }
    public None getReviews() {
        return reviews;
    }

    public void setReviews(None reviews) {
        this.reviews = reviews;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getExpires() {
        return expires;
    }

    public void setExpires(LocalDate expires) {
        this.expires = expires;
    }


}