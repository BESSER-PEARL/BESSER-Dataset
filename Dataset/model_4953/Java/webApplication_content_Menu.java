





import java.util.List;
import java.util.ArrayList;

public class webApplication_content_Menu extends Content {

    private String url;
    private int order;
    private String itemName;



    public webApplication_content_Menu(
        String url,        int order,        String itemName    ) {
        super(
        );
        this.url = url;
        this.order = order;
        this.itemName = itemName;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public String getItemname() {
        return itemName;
    }

    public void setItemname(String itemName) {
        this.itemName = itemName;
    }


}