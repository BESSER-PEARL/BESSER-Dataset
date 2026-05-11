





import java.util.List;
import java.util.ArrayList;

public class eJSL_Library extends Extension {






    private List<eJSL_Entity> ejsl_entitys;


    public eJSL_Library(
    ) {
        super(
        );
        this.ejsl_entitys = new ArrayList<>();
    }

    public eJSL_Library(
        ArrayList<eJSL_Entity> ejsl_entitys    ) {
        this.ejsl_entitys = ejsl_entitys;
    }


    public List<eJSL_Entity> getEjsl_entitys() {
        return ejsl_entitys;
    }

    public void addEjsl_entity(Ejsl_entity ejsl_entity) {
        this.ejsl_entitys.add(ejsl_entity);
    }

}