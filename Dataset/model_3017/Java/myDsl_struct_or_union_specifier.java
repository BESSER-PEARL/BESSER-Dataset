





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_or_union_specifier  {

    private String identifier;





    private myDsl_type_specifier mydsl_type_specifier;


    public myDsl_struct_or_union_specifier(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_type_specifier getMydsl_type_specifier() {
        return mydsl_type_specifier;
    }

    public void setMydsl_type_specifier(myDsl_type_specifier mydsl_type_specifier) {
        this.mydsl_type_specifier = mydsl_type_specifier;
    }

}