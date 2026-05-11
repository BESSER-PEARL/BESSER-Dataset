





import java.util.List;
import java.util.ArrayList;

public class myDsl_DataModel extends Type {

    private String id;





    private myDsl_DataModel mydsl_datamodel;




    private myDsl_DataAccessObject mydsl_dataaccessobject;




    private myDsl_DataAccessObject mydsl_dataaccessobject;


    public myDsl_DataModel(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_DataModel getMydsl_datamodel() {
        return mydsl_datamodel;
    }

    public void setMydsl_datamodel(myDsl_DataModel mydsl_datamodel) {
        this.mydsl_datamodel = mydsl_datamodel;
    }
    public myDsl_DataAccessObject getMydsl_dataaccessobject() {
        return mydsl_dataaccessobject;
    }

    public void setMydsl_dataaccessobject(myDsl_DataAccessObject mydsl_dataaccessobject) {
        this.mydsl_dataaccessobject = mydsl_dataaccessobject;
    }
    public myDsl_DataAccessObject getMydsl_dataaccessobject() {
        return mydsl_dataaccessobject;
    }

    public void setMydsl_dataaccessobject(myDsl_DataAccessObject mydsl_dataaccessobject) {
        this.mydsl_dataaccessobject = mydsl_dataaccessobject;
    }

}