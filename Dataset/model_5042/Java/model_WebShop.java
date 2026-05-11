





import java.util.List;
import java.util.ArrayList;

public class model_WebShop extends IEntity {

    private String webshopVersion;
    private String webshopVendor;



    public model_WebShop(
        String webshopVersion,        String webshopVendor    ) {
        super(
        );
        this.webshopVersion = webshopVersion;
        this.webshopVendor = webshopVendor;
    }


    public String getWebshopversion() {
        return webshopVersion;
    }

    public void setWebshopversion(String webshopVersion) {
        this.webshopVersion = webshopVersion;
    }
    public String getWebshopvendor() {
        return webshopVendor;
    }

    public void setWebshopvendor(String webshopVendor) {
        this.webshopVendor = webshopVendor;
    }


}