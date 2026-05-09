





import java.util.List;
import java.util.ArrayList;

public class domain_Ingredient extends HTMLLayerHolder, UsingMappers {

    private String name;
    private String uid;
    private String layer;





    private List<domain_Component> domain_components;




    private domain_Component domain_component;


    public domain_Ingredient(
        String name,        String uid,        String layer    ) {
        super(
        );
        this.name = name;
        this.uid = uid;
        this.layer = layer;
        this.domain_components = new ArrayList<>();
    }

    public domain_Ingredient(
        String name,        String uid,        String layer        ArrayList<domain_Component> domain_components    ) {
        this.name = name;
        this.uid = uid;
        this.layer = layer;
        this.domain_components = domain_components;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getLayer() {
        return layer;
    }

    public void setLayer(String layer) {
        this.layer = layer;
    }

    public List<domain_Component> getDomain_components() {
        return domain_components;
    }

    public void addDomain_component(Domain_component domain_component) {
        this.domain_components.add(domain_component);
    }
    public domain_Component getDomain_component() {
        return domain_component;
    }

    public void setDomain_component(domain_Component domain_component) {
        this.domain_component = domain_component;
    }

}