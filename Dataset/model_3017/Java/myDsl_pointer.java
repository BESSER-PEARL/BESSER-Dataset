





import java.util.List;
import java.util.ArrayList;

public class myDsl_pointer  {






    private myDsl_pointer mydsl_pointer;




    private myDsl_type_qualifier_list mydsl_type_qualifier_list;




    private myDsl_declarator mydsl_declarator;


    public myDsl_pointer(
    ) {
    }



    public myDsl_pointer getMydsl_pointer() {
        return mydsl_pointer;
    }

    public void setMydsl_pointer(myDsl_pointer mydsl_pointer) {
        this.mydsl_pointer = mydsl_pointer;
    }
    public myDsl_type_qualifier_list getMydsl_type_qualifier_list() {
        return mydsl_type_qualifier_list;
    }

    public void setMydsl_type_qualifier_list(myDsl_type_qualifier_list mydsl_type_qualifier_list) {
        this.mydsl_type_qualifier_list = mydsl_type_qualifier_list;
    }
    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }

}