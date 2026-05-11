





import java.util.List;
import java.util.ArrayList;

public class myDsl_type_qualifier_listR  {

    private String Type_qualifier;





    private myDsl_type_qualifier_list mydsl_type_qualifier_list;




    private List<myDsl_type_qualifier_listR> mydsl_type_qualifier_listrs;


    public myDsl_type_qualifier_listR(
        String Type_qualifier    ) {
        this.Type_qualifier = Type_qualifier;
        this.mydsl_type_qualifier_listrs = new ArrayList<>();
    }

    public myDsl_type_qualifier_listR(
        String Type_qualifier        ArrayList<myDsl_type_qualifier_listR> mydsl_type_qualifier_listrs    ) {
        this.Type_qualifier = Type_qualifier;
        this.mydsl_type_qualifier_listrs = mydsl_type_qualifier_listrs;
    }

    public String getType_qualifier() {
        return Type_qualifier;
    }

    public void setType_qualifier(String Type_qualifier) {
        this.Type_qualifier = Type_qualifier;
    }

    public myDsl_type_qualifier_list getMydsl_type_qualifier_list() {
        return mydsl_type_qualifier_list;
    }

    public void setMydsl_type_qualifier_list(myDsl_type_qualifier_list mydsl_type_qualifier_list) {
        this.mydsl_type_qualifier_list = mydsl_type_qualifier_list;
    }
    public List<myDsl_type_qualifier_listR> getMydsl_type_qualifier_listrs() {
        return mydsl_type_qualifier_listrs;
    }

    public void addMydsl_type_qualifier_listr(Mydsl_type_qualifier_listr mydsl_type_qualifier_listr) {
        this.mydsl_type_qualifier_listrs.add(mydsl_type_qualifier_listr);
    }

}