





import java.util.List;
import java.util.ArrayList;

public class ansic_struct_or_union_specifier  {

    private String struct_or_union;
    private String identifier;





    private ansic_type_specifier ansic_type_specifier;


    public ansic_struct_or_union_specifier(
        String struct_or_union,        String identifier    ) {
        this.struct_or_union = struct_or_union;
        this.identifier = identifier;
    }


    public String getStruct_or_union() {
        return struct_or_union;
    }

    public void setStruct_or_union(String struct_or_union) {
        this.struct_or_union = struct_or_union;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ansic_type_specifier getAnsic_type_specifier() {
        return ansic_type_specifier;
    }

    public void setAnsic_type_specifier(ansic_type_specifier ansic_type_specifier) {
        this.ansic_type_specifier = ansic_type_specifier;
    }

}