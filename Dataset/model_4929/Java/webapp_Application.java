





import java.util.List;
import java.util.ArrayList;

public class webapp_Application extends NamedElement {






    private List<webapp_Collection> webapp_collections;




    private List<webapp_Model> webapp_models;




    private webapp_AbstractView webapp_abstractview;




    private webapp_Model webapp_model;




    private webapp_Collection webapp_collection;




    private List<webapp_AbstractView> webapp_abstractviews;


    public webapp_Application(
    ) {
        super(
        );
        this.webapp_collections = new ArrayList<>();
        this.webapp_models = new ArrayList<>();
        this.webapp_abstractviews = new ArrayList<>();
    }

    public webapp_Application(
        ArrayList<webapp_Collection> webapp_collections,        ArrayList<webapp_Model> webapp_models,        ArrayList<webapp_AbstractView> webapp_abstractviews    ) {
        this.webapp_collections = webapp_collections;
        this.webapp_models = webapp_models;
        this.webapp_abstractviews = webapp_abstractviews;
    }


    public List<webapp_Collection> getWebapp_collections() {
        return webapp_collections;
    }

    public void addWebapp_collection(Webapp_collection webapp_collection) {
        this.webapp_collections.add(webapp_collection);
    }
    public List<webapp_Model> getWebapp_models() {
        return webapp_models;
    }

    public void addWebapp_model(Webapp_model webapp_model) {
        this.webapp_models.add(webapp_model);
    }
    public webapp_AbstractView getWebapp_abstractview() {
        return webapp_abstractview;
    }

    public void setWebapp_abstractview(webapp_AbstractView webapp_abstractview) {
        this.webapp_abstractview = webapp_abstractview;
    }
    public webapp_Model getWebapp_model() {
        return webapp_model;
    }

    public void setWebapp_model(webapp_Model webapp_model) {
        this.webapp_model = webapp_model;
    }
    public webapp_Collection getWebapp_collection() {
        return webapp_collection;
    }

    public void setWebapp_collection(webapp_Collection webapp_collection) {
        this.webapp_collection = webapp_collection;
    }
    public List<webapp_AbstractView> getWebapp_abstractviews() {
        return webapp_abstractviews;
    }

    public void addWebapp_abstractview(Webapp_abstractview webapp_abstractview) {
        this.webapp_abstractviews.add(webapp_abstractview);
    }

}