





import java.util.List;
import java.util.ArrayList;

public class myDsl_specifier_qualifier_list extends type_name, struct_declaration {






    private List<myDsl_specifier_qualifier_list> mydsl_specifier_qualifier_lists;




    private myDsl_type_name mydsl_type_name;


    public myDsl_specifier_qualifier_list(
    ) {
        super(
        );
        this.mydsl_specifier_qualifier_lists = new ArrayList<>();
    }

    public myDsl_specifier_qualifier_list(
        ArrayList<myDsl_specifier_qualifier_list> mydsl_specifier_qualifier_lists    ) {
        this.mydsl_specifier_qualifier_lists = mydsl_specifier_qualifier_lists;
    }


    public List<myDsl_specifier_qualifier_list> getMydsl_specifier_qualifier_lists() {
        return mydsl_specifier_qualifier_lists;
    }

    public void addMydsl_specifier_qualifier_list(Mydsl_specifier_qualifier_list mydsl_specifier_qualifier_list) {
        this.mydsl_specifier_qualifier_lists.add(mydsl_specifier_qualifier_list);
    }
    public myDsl_type_name getMydsl_type_name() {
        return mydsl_type_name;
    }

    public void setMydsl_type_name(myDsl_type_name mydsl_type_name) {
        this.mydsl_type_name = mydsl_type_name;
    }

}