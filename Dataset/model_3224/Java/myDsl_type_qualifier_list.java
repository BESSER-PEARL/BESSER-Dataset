





import java.util.List;
import java.util.ArrayList;

public class myDsl_type_qualifier_list extends direct_abstract_declarator_complement {






    private myDsl_pointer mydsl_pointer;




    private myDsl_type_qualifier mydsl_type_qualifier;


    public myDsl_type_qualifier_list(
    ) {
        super(
        );
    }



    public myDsl_pointer getMydsl_pointer() {
        return mydsl_pointer;
    }

    public void setMydsl_pointer(myDsl_pointer mydsl_pointer) {
        this.mydsl_pointer = mydsl_pointer;
    }
    public myDsl_type_qualifier getMydsl_type_qualifier() {
        return mydsl_type_qualifier;
    }

    public void setMydsl_type_qualifier(myDsl_type_qualifier mydsl_type_qualifier) {
        this.mydsl_type_qualifier = mydsl_type_qualifier;
    }

}