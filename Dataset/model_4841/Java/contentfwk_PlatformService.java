





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PlatformService extends Element {

    private String categoryTRM;
    private String standardClass;





    private contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture;


    public contentfwk_PlatformService(
        String categoryTRM,        String standardClass    ) {
        super(
        );
        this.categoryTRM = categoryTRM;
        this.standardClass = standardClass;
    }


    public String getCategorytrm() {
        return categoryTRM;
    }

    public void setCategorytrm(String categoryTRM) {
        this.categoryTRM = categoryTRM;
    }
    public String getStandardclass() {
        return standardClass;
    }

    public void setStandardclass(String standardClass) {
        this.standardClass = standardClass;
    }

    public contentfwk_TechnologyArchitecture getContentfwk_technologyarchitecture() {
        return contentfwk_technologyarchitecture;
    }

    public void setContentfwk_technologyarchitecture(contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture) {
        this.contentfwk_technologyarchitecture = contentfwk_technologyarchitecture;
    }

}