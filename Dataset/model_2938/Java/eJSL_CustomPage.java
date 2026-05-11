





import java.util.List;
import java.util.ArrayList;

public class eJSL_CustomPage extends Page {

    private String preserve;
    private String pageType;





    private List<eJSL_Entity> ejsl_entitys;


    public eJSL_CustomPage(
        String preserve,        String pageType    ) {
        super(
        );
        this.preserve = preserve;
        this.pageType = pageType;
        this.ejsl_entitys = new ArrayList<>();
    }

    public eJSL_CustomPage(
        String preserve,        String pageType        ArrayList<eJSL_Entity> ejsl_entitys    ) {
        this.preserve = preserve;
        this.pageType = pageType;
        this.ejsl_entitys = ejsl_entitys;
    }

    public String getPreserve() {
        return preserve;
    }

    public void setPreserve(String preserve) {
        this.preserve = preserve;
    }
    public String getPagetype() {
        return pageType;
    }

    public void setPagetype(String pageType) {
        this.pageType = pageType;
    }

    public List<eJSL_Entity> getEjsl_entitys() {
        return ejsl_entitys;
    }

    public void addEjsl_entity(Ejsl_entity ejsl_entity) {
        this.ejsl_entitys.add(ejsl_entity);
    }

}