





import java.util.List;
import java.util.ArrayList;

public class webapp_WebApp extends NamedElement {






    private List<webapp_Model> webapp_models;




    private List<webapp_View> webapp_views;




    private List<webapp_Controller> webapp_controllers;




    private List<webapp_Collection> webapp_collections;




    private List<webapp_Template> webapp_templates;




    private List<webapp_Style> webapp_styles;


    public webapp_WebApp(
    ) {
        super(
        );
        this.webapp_models = new ArrayList<>();
        this.webapp_views = new ArrayList<>();
        this.webapp_controllers = new ArrayList<>();
        this.webapp_collections = new ArrayList<>();
        this.webapp_templates = new ArrayList<>();
        this.webapp_styles = new ArrayList<>();
    }

    public webapp_WebApp(
        ArrayList<webapp_Model> webapp_models,        ArrayList<webapp_View> webapp_views,        ArrayList<webapp_Controller> webapp_controllers,        ArrayList<webapp_Collection> webapp_collections,        ArrayList<webapp_Template> webapp_templates,        ArrayList<webapp_Style> webapp_styles    ) {
        this.webapp_models = webapp_models;
        this.webapp_views = webapp_views;
        this.webapp_controllers = webapp_controllers;
        this.webapp_collections = webapp_collections;
        this.webapp_templates = webapp_templates;
        this.webapp_styles = webapp_styles;
    }


    public List<webapp_Model> getWebapp_models() {
        return webapp_models;
    }

    public void addWebapp_model(Webapp_model webapp_model) {
        this.webapp_models.add(webapp_model);
    }
    public List<webapp_View> getWebapp_views() {
        return webapp_views;
    }

    public void addWebapp_view(Webapp_view webapp_view) {
        this.webapp_views.add(webapp_view);
    }
    public List<webapp_Controller> getWebapp_controllers() {
        return webapp_controllers;
    }

    public void addWebapp_controller(Webapp_controller webapp_controller) {
        this.webapp_controllers.add(webapp_controller);
    }
    public List<webapp_Collection> getWebapp_collections() {
        return webapp_collections;
    }

    public void addWebapp_collection(Webapp_collection webapp_collection) {
        this.webapp_collections.add(webapp_collection);
    }
    public List<webapp_Template> getWebapp_templates() {
        return webapp_templates;
    }

    public void addWebapp_template(Webapp_template webapp_template) {
        this.webapp_templates.add(webapp_template);
    }
    public List<webapp_Style> getWebapp_styles() {
        return webapp_styles;
    }

    public void addWebapp_style(Webapp_style webapp_style) {
        this.webapp_styles.add(webapp_style);
    }

}