





import java.util.List;
import java.util.ArrayList;

public class party_ContactInfo extends DateEffectiveObject {

    private String category;



    public party_ContactInfo(
        String category    ) {
        super(
        );
        this.category = category;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}