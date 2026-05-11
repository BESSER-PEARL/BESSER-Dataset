





import java.util.List;
import java.util.ArrayList;

public class webapp_WebApp extends Named {






    private List<webapp_ServerPage> webapp_serverpages;




    private List<webapp_DataSourceManager> webapp_datasourcemanagers;




    private List<webapp_DataStructure> webapp_datastructures;


    public webapp_WebApp(
    ) {
        super(
        );
        this.webapp_serverpages = new ArrayList<>();
        this.webapp_datasourcemanagers = new ArrayList<>();
        this.webapp_datastructures = new ArrayList<>();
    }

    public webapp_WebApp(
        ArrayList<webapp_ServerPage> webapp_serverpages,        ArrayList<webapp_DataSourceManager> webapp_datasourcemanagers,        ArrayList<webapp_DataStructure> webapp_datastructures    ) {
        this.webapp_serverpages = webapp_serverpages;
        this.webapp_datasourcemanagers = webapp_datasourcemanagers;
        this.webapp_datastructures = webapp_datastructures;
    }


    public List<webapp_ServerPage> getWebapp_serverpages() {
        return webapp_serverpages;
    }

    public void addWebapp_serverpage(Webapp_serverpage webapp_serverpage) {
        this.webapp_serverpages.add(webapp_serverpage);
    }
    public List<webapp_DataSourceManager> getWebapp_datasourcemanagers() {
        return webapp_datasourcemanagers;
    }

    public void addWebapp_datasourcemanager(Webapp_datasourcemanager webapp_datasourcemanager) {
        this.webapp_datasourcemanagers.add(webapp_datasourcemanager);
    }
    public List<webapp_DataStructure> getWebapp_datastructures() {
        return webapp_datastructures;
    }

    public void addWebapp_datastructure(Webapp_datastructure webapp_datastructure) {
        this.webapp_datastructures.add(webapp_datastructure);
    }

}