





import java.util.List;
import java.util.ArrayList;

public class myDsl_Feature  {

    private boolean many;
    private String name;





    private myDsl_DataModel mydsl_datamodel;




    private myDsl_RestModel mydsl_restmodel;


    public myDsl_Feature(
        boolean many,        String name    ) {
        this.many = many;
        this.name = name;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_DataModel getMydsl_datamodel() {
        return mydsl_datamodel;
    }

    public void setMydsl_datamodel(myDsl_DataModel mydsl_datamodel) {
        this.mydsl_datamodel = mydsl_datamodel;
    }
    public myDsl_RestModel getMydsl_restmodel() {
        return mydsl_restmodel;
    }

    public void setMydsl_restmodel(myDsl_RestModel mydsl_restmodel) {
        this.mydsl_restmodel = mydsl_restmodel;
    }

}