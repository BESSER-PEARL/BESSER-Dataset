





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_System extends BasicElement {






    private List<aspectualacme_Connector> aspectualacme_connectors;




    private List<aspectualacme_Property> aspectualacme_propertys;




    private List<aspectualacme_Family> aspectualacme_familys;




    private aspectualacme_Component aspectualacme_component;




    private List<aspectualacme_Component> aspectualacme_components;




    private aspectualacme_Representation aspectualacme_representation;




    private aspectualacme_Connector aspectualacme_connector;




    private aspectualacme_Property aspectualacme_property;




    private aspectualacme_Representation aspectualacme_representation;


    public aspectualacme_System(
    ) {
        super(
        );
        this.aspectualacme_connectors = new ArrayList<>();
        this.aspectualacme_propertys = new ArrayList<>();
        this.aspectualacme_familys = new ArrayList<>();
        this.aspectualacme_components = new ArrayList<>();
    }

    public aspectualacme_System(
        ArrayList<aspectualacme_Connector> aspectualacme_connectors,        ArrayList<aspectualacme_Property> aspectualacme_propertys,        ArrayList<aspectualacme_Family> aspectualacme_familys,        ArrayList<aspectualacme_Component> aspectualacme_components    ) {
        this.aspectualacme_connectors = aspectualacme_connectors;
        this.aspectualacme_propertys = aspectualacme_propertys;
        this.aspectualacme_familys = aspectualacme_familys;
        this.aspectualacme_components = aspectualacme_components;
    }


    public List<aspectualacme_Connector> getAspectualacme_connectors() {
        return aspectualacme_connectors;
    }

    public void addAspectualacme_connector(Aspectualacme_connector aspectualacme_connector) {
        this.aspectualacme_connectors.add(aspectualacme_connector);
    }
    public List<aspectualacme_Property> getAspectualacme_propertys() {
        return aspectualacme_propertys;
    }

    public void addAspectualacme_property(Aspectualacme_property aspectualacme_property) {
        this.aspectualacme_propertys.add(aspectualacme_property);
    }
    public List<aspectualacme_Family> getAspectualacme_familys() {
        return aspectualacme_familys;
    }

    public void addAspectualacme_family(Aspectualacme_family aspectualacme_family) {
        this.aspectualacme_familys.add(aspectualacme_family);
    }
    public aspectualacme_Component getAspectualacme_component() {
        return aspectualacme_component;
    }

    public void setAspectualacme_component(aspectualacme_Component aspectualacme_component) {
        this.aspectualacme_component = aspectualacme_component;
    }
    public List<aspectualacme_Component> getAspectualacme_components() {
        return aspectualacme_components;
    }

    public void addAspectualacme_component(Aspectualacme_component aspectualacme_component) {
        this.aspectualacme_components.add(aspectualacme_component);
    }
    public aspectualacme_Representation getAspectualacme_representation() {
        return aspectualacme_representation;
    }

    public void setAspectualacme_representation(aspectualacme_Representation aspectualacme_representation) {
        this.aspectualacme_representation = aspectualacme_representation;
    }
    public aspectualacme_Connector getAspectualacme_connector() {
        return aspectualacme_connector;
    }

    public void setAspectualacme_connector(aspectualacme_Connector aspectualacme_connector) {
        this.aspectualacme_connector = aspectualacme_connector;
    }
    public aspectualacme_Property getAspectualacme_property() {
        return aspectualacme_property;
    }

    public void setAspectualacme_property(aspectualacme_Property aspectualacme_property) {
        this.aspectualacme_property = aspectualacme_property;
    }
    public aspectualacme_Representation getAspectualacme_representation() {
        return aspectualacme_representation;
    }

    public void setAspectualacme_representation(aspectualacme_Representation aspectualacme_representation) {
        this.aspectualacme_representation = aspectualacme_representation;
    }

}