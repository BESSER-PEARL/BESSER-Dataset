





import java.util.List;
import java.util.ArrayList;

public class owl_Property extends RDFProperty {

    private String functional;
    private String deprecated;





    private List<owl_Property> owl_propertys;




    private List<owl_Property> owl_propertys;


    public owl_Property(
        String functional,        String deprecated    ) {
        super(
        );
        this.functional = functional;
        this.deprecated = deprecated;
        this.owl_propertys = new ArrayList<>();
        this.owl_propertys = new ArrayList<>();
    }

    public owl_Property(
        String functional,        String deprecated        ArrayList<owl_Property> owl_propertys,        ArrayList<owl_Property> owl_propertys    ) {
        this.functional = functional;
        this.deprecated = deprecated;
        this.owl_propertys = owl_propertys;
        this.owl_propertys = owl_propertys;
    }

    public String getFunctional() {
        return functional;
    }

    public void setFunctional(String functional) {
        this.functional = functional;
    }
    public String getDeprecated() {
        return deprecated;
    }

    public void setDeprecated(String deprecated) {
        this.deprecated = deprecated;
    }

    public List<owl_Property> getOwl_propertys() {
        return owl_propertys;
    }

    public void addOwl_property(Owl_property owl_property) {
        this.owl_propertys.add(owl_property);
    }
    public List<owl_Property> getOwl_propertys() {
        return owl_propertys;
    }

    public void addOwl_property(Owl_property owl_property) {
        this.owl_propertys.add(owl_property);
    }

}