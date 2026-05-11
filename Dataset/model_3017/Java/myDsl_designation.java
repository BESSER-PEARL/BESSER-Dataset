





import java.util.List;
import java.util.ArrayList;

public class myDsl_designation  {






    private myDsl_designator_list mydsl_designator_list;




    private myDsl_initializer_list mydsl_initializer_list;


    public myDsl_designation(
    ) {
    }



    public myDsl_designator_list getMydsl_designator_list() {
        return mydsl_designator_list;
    }

    public void setMydsl_designator_list(myDsl_designator_list mydsl_designator_list) {
        this.mydsl_designator_list = mydsl_designator_list;
    }
    public myDsl_initializer_list getMydsl_initializer_list() {
        return mydsl_initializer_list;
    }

    public void setMydsl_initializer_list(myDsl_initializer_list mydsl_initializer_list) {
        this.mydsl_initializer_list = mydsl_initializer_list;
    }

}