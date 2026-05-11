





import java.util.List;
import java.util.ArrayList;

public class myDsl_Service  {

    private String updateby;
    private String findby;
    private String name;
    private String deleteby;





    private List<myDsl_DataAccessObject> mydsl_dataaccessobjects;




    private myDsl_RestAPI mydsl_restapi;




    private myDsl_DataModel mydsl_datamodel;




    private myDsl_Resource mydsl_resource;




    private myDsl_DataModel mydsl_datamodel;


    public myDsl_Service(
        String updateby,        String findby,        String name,        String deleteby    ) {
        this.updateby = updateby;
        this.findby = findby;
        this.name = name;
        this.deleteby = deleteby;
        this.mydsl_dataaccessobjects = new ArrayList<>();
    }

    public myDsl_Service(
        String updateby,        String findby,        String name,        String deleteby        ArrayList<myDsl_DataAccessObject> mydsl_dataaccessobjects    ) {
        this.updateby = updateby;
        this.findby = findby;
        this.name = name;
        this.deleteby = deleteby;
        this.mydsl_dataaccessobjects = mydsl_dataaccessobjects;
    }

    public String getUpdateby() {
        return updateby;
    }

    public void setUpdateby(String updateby) {
        this.updateby = updateby;
    }
    public String getFindby() {
        return findby;
    }

    public void setFindby(String findby) {
        this.findby = findby;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDeleteby() {
        return deleteby;
    }

    public void setDeleteby(String deleteby) {
        this.deleteby = deleteby;
    }

    public List<myDsl_DataAccessObject> getMydsl_dataaccessobjects() {
        return mydsl_dataaccessobjects;
    }

    public void addMydsl_dataaccessobject(Mydsl_dataaccessobject mydsl_dataaccessobject) {
        this.mydsl_dataaccessobjects.add(mydsl_dataaccessobject);
    }
    public myDsl_RestAPI getMydsl_restapi() {
        return mydsl_restapi;
    }

    public void setMydsl_restapi(myDsl_RestAPI mydsl_restapi) {
        this.mydsl_restapi = mydsl_restapi;
    }
    public myDsl_DataModel getMydsl_datamodel() {
        return mydsl_datamodel;
    }

    public void setMydsl_datamodel(myDsl_DataModel mydsl_datamodel) {
        this.mydsl_datamodel = mydsl_datamodel;
    }
    public myDsl_Resource getMydsl_resource() {
        return mydsl_resource;
    }

    public void setMydsl_resource(myDsl_Resource mydsl_resource) {
        this.mydsl_resource = mydsl_resource;
    }
    public myDsl_DataModel getMydsl_datamodel() {
        return mydsl_datamodel;
    }

    public void setMydsl_datamodel(myDsl_DataModel mydsl_datamodel) {
        this.mydsl_datamodel = mydsl_datamodel;
    }

}