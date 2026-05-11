





import java.util.List;
import java.util.ArrayList;

public class myDsl_RestAPI  {






    private myDsl_DomainModel mydsl_domainmodel;




    private List<myDsl_DataAccessObject> mydsl_dataaccessobjects;




    private List<myDsl_ExceptionMapper> mydsl_exceptionmappers;


    public myDsl_RestAPI(
    ) {
        this.mydsl_dataaccessobjects = new ArrayList<>();
        this.mydsl_exceptionmappers = new ArrayList<>();
    }

    public myDsl_RestAPI(
        ArrayList<myDsl_DataAccessObject> mydsl_dataaccessobjects,        ArrayList<myDsl_ExceptionMapper> mydsl_exceptionmappers    ) {
        this.mydsl_dataaccessobjects = mydsl_dataaccessobjects;
        this.mydsl_exceptionmappers = mydsl_exceptionmappers;
    }


    public myDsl_DomainModel getMydsl_domainmodel() {
        return mydsl_domainmodel;
    }

    public void setMydsl_domainmodel(myDsl_DomainModel mydsl_domainmodel) {
        this.mydsl_domainmodel = mydsl_domainmodel;
    }
    public List<myDsl_DataAccessObject> getMydsl_dataaccessobjects() {
        return mydsl_dataaccessobjects;
    }

    public void addMydsl_dataaccessobject(Mydsl_dataaccessobject mydsl_dataaccessobject) {
        this.mydsl_dataaccessobjects.add(mydsl_dataaccessobject);
    }
    public List<myDsl_ExceptionMapper> getMydsl_exceptionmappers() {
        return mydsl_exceptionmappers;
    }

    public void addMydsl_exceptionmapper(Mydsl_exceptionmapper mydsl_exceptionmapper) {
        this.mydsl_exceptionmappers.add(mydsl_exceptionmapper);
    }

}