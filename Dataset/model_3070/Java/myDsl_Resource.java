





import java.util.List;
import java.util.ArrayList;

public class myDsl_Resource  {

    private String updateby;
    private String name;
    private String findby;
    private String deleteby;





    private myDsl_RestModel mydsl_restmodel;




    private myDsl_RestModel mydsl_restmodel;




    private myDsl_RestAPI mydsl_restapi;




    private myDsl_ExceptionMapper mydsl_exceptionmapper;


    public myDsl_Resource(
        String updateby,        String name,        String findby,        String deleteby    ) {
        this.updateby = updateby;
        this.name = name;
        this.findby = findby;
        this.deleteby = deleteby;
    }


    public String getUpdateby() {
        return updateby;
    }

    public void setUpdateby(String updateby) {
        this.updateby = updateby;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFindby() {
        return findby;
    }

    public void setFindby(String findby) {
        this.findby = findby;
    }
    public String getDeleteby() {
        return deleteby;
    }

    public void setDeleteby(String deleteby) {
        this.deleteby = deleteby;
    }

    public myDsl_RestModel getMydsl_restmodel() {
        return mydsl_restmodel;
    }

    public void setMydsl_restmodel(myDsl_RestModel mydsl_restmodel) {
        this.mydsl_restmodel = mydsl_restmodel;
    }
    public myDsl_RestModel getMydsl_restmodel() {
        return mydsl_restmodel;
    }

    public void setMydsl_restmodel(myDsl_RestModel mydsl_restmodel) {
        this.mydsl_restmodel = mydsl_restmodel;
    }
    public myDsl_RestAPI getMydsl_restapi() {
        return mydsl_restapi;
    }

    public void setMydsl_restapi(myDsl_RestAPI mydsl_restapi) {
        this.mydsl_restapi = mydsl_restapi;
    }
    public myDsl_ExceptionMapper getMydsl_exceptionmapper() {
        return mydsl_exceptionmapper;
    }

    public void setMydsl_exceptionmapper(myDsl_ExceptionMapper mydsl_exceptionmapper) {
        this.mydsl_exceptionmapper = mydsl_exceptionmapper;
    }

}