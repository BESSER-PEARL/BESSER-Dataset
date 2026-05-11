





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PlatformService extends Element, Service {

    private String categoryTRM;





    private contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture;


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

    public contentfwk_TechnologyArchitecture getContentfwk_technologyarchitecture() {
        return contentfwk_technologyarchitecture;
    }

    public void setContentfwk_technologyarchitecture(contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture) {
        this.contentfwk_technologyarchitecture = contentfwk_technologyarchitecture;
    }

}