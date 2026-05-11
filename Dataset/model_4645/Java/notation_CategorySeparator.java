





import java.util.List;
import java.util.ArrayList;

public class notation_CategorySeparator extends Node {

    private String newChildIcon;
    private String newChildCodeSyncType;
    private String category;



    public notation_CategorySeparator(
        String newChildIcon,        String newChildCodeSyncType,        String category    ) {
        super(
        );
        this.newChildIcon = newChildIcon;
        this.newChildCodeSyncType = newChildCodeSyncType;
        this.category = category;
    }


    public String getNewchildicon() {
        return newChildIcon;
    }

    public void setNewchildicon(String newChildIcon) {
        this.newChildIcon = newChildIcon;
    }
    public String getNewchildcodesynctype() {
        return newChildCodeSyncType;
    }

    public void setNewchildcodesynctype(String newChildCodeSyncType) {
        this.newChildCodeSyncType = newChildCodeSyncType;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}