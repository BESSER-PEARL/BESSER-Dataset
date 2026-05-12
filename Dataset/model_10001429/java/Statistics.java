





import java.util.List;
import java.util.ArrayList;

public class Statistics  {

    private int item_id;
    private int clicks;
    private int click_subCat;
    private int click_homeCat;
    private int click_homepage;
    private int customer_id;



    public Statistics(
        int item_id,        int clicks,        int click_subCat,        int click_homeCat,        int click_homepage,        int customer_id    ) {
        this.item_id = item_id;
        this.clicks = clicks;
        this.click_subCat = click_subCat;
        this.click_homeCat = click_homeCat;
        this.click_homepage = click_homepage;
        this.customer_id = customer_id;
    }


    public int getItem_id() {
        return item_id;
    }

    public void setItem_id(int item_id) {
        this.item_id = item_id;
    }
    public int getClicks() {
        return clicks;
    }

    public void setClicks(int clicks) {
        this.clicks = clicks;
    }
    public int getClick_subcat() {
        return click_subCat;
    }

    public void setClick_subcat(int click_subCat) {
        this.click_subCat = click_subCat;
    }
    public int getClick_homecat() {
        return click_homeCat;
    }

    public void setClick_homecat(int click_homeCat) {
        this.click_homeCat = click_homeCat;
    }
    public int getClick_homepage() {
        return click_homepage;
    }

    public void setClick_homepage(int click_homepage) {
        this.click_homepage = click_homepage;
    }
    public int getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(int customer_id) {
        this.customer_id = customer_id;
    }


}