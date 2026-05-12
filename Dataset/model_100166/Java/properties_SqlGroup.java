





import java.util.List;
import java.util.ArrayList;

public class properties_SqlGroup  {

    private String description;
    private String id;





    private List<properties_SqlQuery> properties_sqlquerys;




    private List<properties_SqlFile> properties_sqlfiles;




    private List<properties_SpecificDBMSProperties> properties_specificdbmspropertiess;




    private properties_SqlProperties properties_sqlproperties;


    public properties_SqlGroup(
        String description,        String id    ) {
        this.description = description;
        this.id = id;
        this.properties_sqlquerys = new ArrayList<>();
        this.properties_sqlfiles = new ArrayList<>();
        this.properties_specificdbmspropertiess = new ArrayList<>();
    }

    public properties_SqlGroup(
        String description,        String id        ArrayList<properties_SqlQuery> properties_sqlquerys,        ArrayList<properties_SqlFile> properties_sqlfiles,        ArrayList<properties_SpecificDBMSProperties> properties_specificdbmspropertiess    ) {
        this.description = description;
        this.id = id;
        this.properties_sqlquerys = properties_sqlquerys;
        this.properties_sqlfiles = properties_sqlfiles;
        this.properties_specificdbmspropertiess = properties_specificdbmspropertiess;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<properties_SqlQuery> getProperties_sqlquerys() {
        return properties_sqlquerys;
    }

    public void addProperties_sqlquery(Properties_sqlquery properties_sqlquery) {
        this.properties_sqlquerys.add(properties_sqlquery);
    }
    public List<properties_SqlFile> getProperties_sqlfiles() {
        return properties_sqlfiles;
    }

    public void addProperties_sqlfile(Properties_sqlfile properties_sqlfile) {
        this.properties_sqlfiles.add(properties_sqlfile);
    }
    public List<properties_SpecificDBMSProperties> getProperties_specificdbmspropertiess() {
        return properties_specificdbmspropertiess;
    }

    public void addProperties_specificdbmsproperties(Properties_specificdbmsproperties properties_specificdbmsproperties) {
        this.properties_specificdbmspropertiess.add(properties_specificdbmsproperties);
    }
    public properties_SqlProperties getProperties_sqlproperties() {
        return properties_sqlproperties;
    }

    public void setProperties_sqlproperties(properties_SqlProperties properties_sqlproperties) {
        this.properties_sqlproperties = properties_sqlproperties;
    }

}