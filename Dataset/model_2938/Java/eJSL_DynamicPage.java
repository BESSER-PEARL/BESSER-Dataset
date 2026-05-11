





import java.util.List;
import java.util.ArrayList;

public class eJSL_DynamicPage extends Page {

    private boolean preserve;





    private List<eJSL_Entity> ejsl_entitys;


    public eJSL_DynamicPage(
        boolean preserve    ) {
        super(
        );
        this.preserve = preserve;
        this.ejsl_entitys = new ArrayList<>();
    }

    public eJSL_DynamicPage(
        boolean preserve        ArrayList<eJSL_Entity> ejsl_entitys    ) {
        this.preserve = preserve;
        this.ejsl_entitys = ejsl_entitys;
    }

    public boolean getPreserve() {
        return preserve;
    }

    public void setPreserve(boolean preserve) {
        this.preserve = preserve;
    }

    public List<eJSL_Entity> getEjsl_entitys() {
        return ejsl_entitys;
    }

    public void addEjsl_entity(Ejsl_entity ejsl_entity) {
        this.ejsl_entitys.add(ejsl_entity);
    }

}