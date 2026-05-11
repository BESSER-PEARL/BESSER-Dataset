





import java.util.List;
import java.util.ArrayList;

public class myDsl_init_declarator  {






    private myDsl_declarator mydsl_declarator;




    private myDsl_init_declarator_list mydsl_init_declarator_list;


    public myDsl_init_declarator(
    ) {
    }



    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }
    public myDsl_init_declarator_list getMydsl_init_declarator_list() {
        return mydsl_init_declarator_list;
    }

    public void setMydsl_init_declarator_list(myDsl_init_declarator_list mydsl_init_declarator_list) {
        this.mydsl_init_declarator_list = mydsl_init_declarator_list;
    }

}