





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_Family extends BasicElement {






    private aspectualacme_BasicElement aspectualacme_basicelement;




    private List<aspectualacme_Property> aspectualacme_propertys;




    private aspectualacme_Component aspectualacme_component;




    private aspectualacme_Property aspectualacme_property;




    private aspectualacme_Connector aspectualacme_connector;




    private List<aspectualacme_Component> aspectualacme_components;




    private List<aspectualacme_Connector> aspectualacme_connectors;


    public aspectualacme_Family(
    ) {
        super(
        );
        this.aspectualacme_propertys = new ArrayList<>();
        this.aspectualacme_components = new ArrayList<>();
        this.aspectualacme_connectors = new ArrayList<>();
    }

    public aspectualacme_Family(
        ArrayList<aspectualacme_Property> aspectualacme_propertys,        ArrayList<aspectualacme_Component> aspectualacme_components,        ArrayList<aspectualacme_Connector> aspectualacme_connectors    ) {
        this.aspectualacme_propertys = aspectualacme_propertys;
        this.aspectualacme_components = aspectualacme_components;
        this.aspectualacme_connectors = aspectualacme_connectors;
    }


    public aspectualacme_BasicElement getAspectualacme_basicelement() {
        return aspectualacme_basicelement;
    }

    public void setAspectualacme_basicelement(aspectualacme_BasicElement aspectualacme_basicelement) {
        this.aspectualacme_basicelement = aspectualacme_basicelement;
    }
    public List<aspectualacme_Property> getAspectualacme_propertys() {
        return aspectualacme_propertys;
    }

    public void addAspectualacme_property(Aspectualacme_property aspectualacme_property) {
        this.aspectualacme_propertys.add(aspectualacme_property);
    }
    public aspectualacme_Component getAspectualacme_component() {
        return aspectualacme_component;
    }

    public void setAspectualacme_component(aspectualacme_Component aspectualacme_component) {
        this.aspectualacme_component = aspectualacme_component;
    }
    public aspectualacme_Property getAspectualacme_property() {
        return aspectualacme_property;
    }

    public void setAspectualacme_property(aspectualacme_Property aspectualacme_property) {
        this.aspectualacme_property = aspectualacme_property;
    }
    public aspectualacme_Connector getAspectualacme_connector() {
        return aspectualacme_connector;
    }

    public void setAspectualacme_connector(aspectualacme_Connector aspectualacme_connector) {
        this.aspectualacme_connector = aspectualacme_connector;
    }
    public List<aspectualacme_Component> getAspectualacme_components() {
        return aspectualacme_components;
    }

    public void addAspectualacme_component(Aspectualacme_component aspectualacme_component) {
        this.aspectualacme_components.add(aspectualacme_component);
    }
    public List<aspectualacme_Connector> getAspectualacme_connectors() {
        return aspectualacme_connectors;
    }

    public void addAspectualacme_connector(Aspectualacme_connector aspectualacme_connector) {
        this.aspectualacme_connectors.add(aspectualacme_connector);
    }

}