





import java.util.List;
import java.util.ArrayList;

public class myDsl_Transformation  {






    private myDsl_ModelMapper mydsl_modelmapper;




    private myDsl_DataModel mydsl_datamodel;




    private myDsl_RestModel mydsl_restmodel;


    public myDsl_Transformation(
    ) {
    }



    public myDsl_ModelMapper getMydsl_modelmapper() {
        return mydsl_modelmapper;
    }

    public void setMydsl_modelmapper(myDsl_ModelMapper mydsl_modelmapper) {
        this.mydsl_modelmapper = mydsl_modelmapper;
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