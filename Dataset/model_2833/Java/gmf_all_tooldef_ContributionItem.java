





import java.util.List;
import java.util.ArrayList;

public class gmf_all_tooldef_ContributionItem extends ItemBase {

    private String title;





    private Image image;


    public gmf_all_tooldef_ContributionItem(
        String title    ) {
        super(
        );
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Image getImage() {
        return image;
    }

    public void setImage(Image image) {
        this.image = image;
    }

}