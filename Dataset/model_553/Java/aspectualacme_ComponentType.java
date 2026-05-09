





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ComponentType extends TypeDefinition {






    private aspectualacme_Family aspectualacme_family;




    private aspectualacme_Component aspectualacme_component;




    private List<aspectualacme_ComponentType> aspectualacme_componenttypes;




    private aspectualacme_Component aspectualacme_component;




    private aspectualacme_Family aspectualacme_family;


    public aspectualacme_ComponentType(
    ) {
        super(
        );
        this.aspectualacme_componenttypes = new ArrayList<>();
    }

    public aspectualacme_ComponentType(
        ArrayList<aspectualacme_ComponentType> aspectualacme_componenttypes    ) {
        this.aspectualacme_componenttypes = aspectualacme_componenttypes;
    }


    public aspectualacme_Family getAspectualacme_family() {
        return aspectualacme_family;
    }

    public void setAspectualacme_family(aspectualacme_Family aspectualacme_family) {
        this.aspectualacme_family = aspectualacme_family;
    }
    public aspectualacme_Component getAspectualacme_component() {
        return aspectualacme_component;
    }

    public void setAspectualacme_component(aspectualacme_Component aspectualacme_component) {
        this.aspectualacme_component = aspectualacme_component;
    }
    public List<aspectualacme_ComponentType> getAspectualacme_componenttypes() {
        return aspectualacme_componenttypes;
    }

    public void addAspectualacme_componenttype(Aspectualacme_componenttype aspectualacme_componenttype) {
        this.aspectualacme_componenttypes.add(aspectualacme_componenttype);
    }
    public aspectualacme_Component getAspectualacme_component() {
        return aspectualacme_component;
    }

    public void setAspectualacme_component(aspectualacme_Component aspectualacme_component) {
        this.aspectualacme_component = aspectualacme_component;
    }
    public aspectualacme_Family getAspectualacme_family() {
        return aspectualacme_family;
    }

    public void setAspectualacme_family(aspectualacme_Family aspectualacme_family) {
        this.aspectualacme_family = aspectualacme_family;
    }

}