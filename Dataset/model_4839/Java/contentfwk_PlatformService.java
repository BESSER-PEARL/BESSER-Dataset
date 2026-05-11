





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PlatformService extends Service, Element {

    private String categoryTRM;



    public contentfwk_PlatformService(
        String categoryTRM    ) {
        super(
        );
        this.categoryTRM = categoryTRM;
    }


    public String getCategorytrm() {
        return categoryTRM;
    }

    public void setCategorytrm(String categoryTRM) {
        this.categoryTRM = categoryTRM;
    }


}