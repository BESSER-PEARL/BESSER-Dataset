





import java.util.List;
import java.util.ArrayList;

public class webapp_Resource  {






    private List<webapp_Image> webapp_images;




    private List<webapp_File> webapp_files;




    private webapp_WebApp webapp_webapp;




    private List<webapp_Properties> webapp_propertiess;


    public webapp_Resource(
    ) {
        this.webapp_images = new ArrayList<>();
        this.webapp_files = new ArrayList<>();
        this.webapp_propertiess = new ArrayList<>();
    }

    public webapp_Resource(
        ArrayList<webapp_Image> webapp_images,        ArrayList<webapp_File> webapp_files,        ArrayList<webapp_Properties> webapp_propertiess    ) {
        this.webapp_images = webapp_images;
        this.webapp_files = webapp_files;
        this.webapp_propertiess = webapp_propertiess;
    }


    public List<webapp_Image> getWebapp_images() {
        return webapp_images;
    }

    public void addWebapp_image(Webapp_image webapp_image) {
        this.webapp_images.add(webapp_image);
    }
    public List<webapp_File> getWebapp_files() {
        return webapp_files;
    }

    public void addWebapp_file(Webapp_file webapp_file) {
        this.webapp_files.add(webapp_file);
    }
    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }
    public List<webapp_Properties> getWebapp_propertiess() {
        return webapp_propertiess;
    }

    public void addWebapp_properties(Webapp_properties webapp_properties) {
        this.webapp_propertiess.add(webapp_properties);
    }

}