





import java.util.List;
import java.util.ArrayList;

public class ddsm_ChefResource extends Resource {

    private String cookbookId;



    public ddsm_ChefResource(
        String cookbookId    ) {
        super(
        );
        this.cookbookId = cookbookId;
    }


    public String getCookbookid() {
        return cookbookId;
    }

    public void setCookbookid(String cookbookId) {
        this.cookbookId = cookbookId;
    }


}