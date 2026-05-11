





import java.util.List;
import java.util.ArrayList;

public class myDsl_initializer  {






    private myDsl_init_declarator mydsl_init_declarator;




    private myDsl_initializer_listR mydsl_initializer_listr;




    private myDsl_initializer_list mydsl_initializer_list;


    public myDsl_initializer(
    ) {
    }



    public myDsl_init_declarator getMydsl_init_declarator() {
        return mydsl_init_declarator;
    }

    public void setMydsl_init_declarator(myDsl_init_declarator mydsl_init_declarator) {
        this.mydsl_init_declarator = mydsl_init_declarator;
    }
    public myDsl_initializer_listR getMydsl_initializer_listr() {
        return mydsl_initializer_listr;
    }

    public void setMydsl_initializer_listr(myDsl_initializer_listR mydsl_initializer_listr) {
        this.mydsl_initializer_listr = mydsl_initializer_listr;
    }
    public myDsl_initializer_list getMydsl_initializer_list() {
        return mydsl_initializer_list;
    }

    public void setMydsl_initializer_list(myDsl_initializer_list mydsl_initializer_list) {
        this.mydsl_initializer_list = mydsl_initializer_list;
    }

}