





import java.util.List;
import java.util.ArrayList;

public class myDsl_parameter_listR  {






    private List<myDsl_parameter_listR> mydsl_parameter_listrs;




    private myDsl_parameter_list mydsl_parameter_list;




    private myDsl_parameter_declaration mydsl_parameter_declaration;


    public myDsl_parameter_listR(
    ) {
        this.mydsl_parameter_listrs = new ArrayList<>();
    }

    public myDsl_parameter_listR(
        ArrayList<myDsl_parameter_listR> mydsl_parameter_listrs    ) {
        this.mydsl_parameter_listrs = mydsl_parameter_listrs;
    }


    public List<myDsl_parameter_listR> getMydsl_parameter_listrs() {
        return mydsl_parameter_listrs;
    }

    public void addMydsl_parameter_listr(Mydsl_parameter_listr mydsl_parameter_listr) {
        this.mydsl_parameter_listrs.add(mydsl_parameter_listr);
    }
    public myDsl_parameter_list getMydsl_parameter_list() {
        return mydsl_parameter_list;
    }

    public void setMydsl_parameter_list(myDsl_parameter_list mydsl_parameter_list) {
        this.mydsl_parameter_list = mydsl_parameter_list;
    }
    public myDsl_parameter_declaration getMydsl_parameter_declaration() {
        return mydsl_parameter_declaration;
    }

    public void setMydsl_parameter_declaration(myDsl_parameter_declaration mydsl_parameter_declaration) {
        this.mydsl_parameter_declaration = mydsl_parameter_declaration;
    }

}