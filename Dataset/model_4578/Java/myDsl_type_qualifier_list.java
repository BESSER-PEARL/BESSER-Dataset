





import java.util.List;
import java.util.ArrayList;

public class myDsl_type_qualifier_list extends pointer {

    private String Type_qualifier;





    private myDsl_pointer mydsl_pointer;




    private myDsl_direct_declaratorR mydsl_direct_declaratorr;


    public myDsl_type_qualifier_list(
        String Type_qualifier    ) {
        super(
        );
        this.Type_qualifier = Type_qualifier;
    }


    public String getType_qualifier() {
        return Type_qualifier;
    }

    public void setType_qualifier(String Type_qualifier) {
        this.Type_qualifier = Type_qualifier;
    }

    public myDsl_pointer getMydsl_pointer() {
        return mydsl_pointer;
    }

    public void setMydsl_pointer(myDsl_pointer mydsl_pointer) {
        this.mydsl_pointer = mydsl_pointer;
    }
    public myDsl_direct_declaratorR getMydsl_direct_declaratorr() {
        return mydsl_direct_declaratorr;
    }

    public void setMydsl_direct_declaratorr(myDsl_direct_declaratorR mydsl_direct_declaratorr) {
        this.mydsl_direct_declaratorr = mydsl_direct_declaratorr;
    }

}