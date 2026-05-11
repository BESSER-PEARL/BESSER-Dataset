





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_declarator_listR  {






    private myDsl_struct_declarator_list mydsl_struct_declarator_list;




    private myDsl_struct_declarator mydsl_struct_declarator;




    private List<myDsl_struct_declarator_listR> mydsl_struct_declarator_listrs;


    public myDsl_struct_declarator_listR(
    ) {
        this.mydsl_struct_declarator_listrs = new ArrayList<>();
    }

    public myDsl_struct_declarator_listR(
        ArrayList<myDsl_struct_declarator_listR> mydsl_struct_declarator_listrs    ) {
        this.mydsl_struct_declarator_listrs = mydsl_struct_declarator_listrs;
    }


    public myDsl_struct_declarator_list getMydsl_struct_declarator_list() {
        return mydsl_struct_declarator_list;
    }

    public void setMydsl_struct_declarator_list(myDsl_struct_declarator_list mydsl_struct_declarator_list) {
        this.mydsl_struct_declarator_list = mydsl_struct_declarator_list;
    }
    public myDsl_struct_declarator getMydsl_struct_declarator() {
        return mydsl_struct_declarator;
    }

    public void setMydsl_struct_declarator(myDsl_struct_declarator mydsl_struct_declarator) {
        this.mydsl_struct_declarator = mydsl_struct_declarator;
    }
    public List<myDsl_struct_declarator_listR> getMydsl_struct_declarator_listrs() {
        return mydsl_struct_declarator_listrs;
    }

    public void addMydsl_struct_declarator_listr(Mydsl_struct_declarator_listr mydsl_struct_declarator_listr) {
        this.mydsl_struct_declarator_listrs.add(mydsl_struct_declarator_listr);
    }

}