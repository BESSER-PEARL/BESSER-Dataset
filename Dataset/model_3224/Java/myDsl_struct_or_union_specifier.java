





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_or_union_specifier  {

    private String identifier;
    private String struct_or_union;





    private myDsl_type_specifier mydsl_type_specifier;


    public myDsl_struct_or_union_specifier(
        String identifier,        String struct_or_union    ) {
        this.identifier = identifier;
        this.struct_or_union = struct_or_union;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getStruct_or_union() {
        return struct_or_union;
    }

    public void setStruct_or_union(String struct_or_union) {
        this.struct_or_union = struct_or_union;
    }

    public myDsl_type_specifier getMydsl_type_specifier() {
        return mydsl_type_specifier;
    }

    public void setMydsl_type_specifier(myDsl_type_specifier mydsl_type_specifier) {
        this.mydsl_type_specifier = mydsl_type_specifier;
    }

}