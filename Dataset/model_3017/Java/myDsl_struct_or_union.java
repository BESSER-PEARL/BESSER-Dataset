





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_or_union extends struct_or_union_specifier {

    private String struct;
    private String union;





    private myDsl_struct_or_union_specifier mydsl_struct_or_union_specifier;


    public myDsl_struct_or_union(
        String struct,        String union    ) {
        super(
        );
        this.struct = struct;
        this.union = union;
    }


    public String getStruct() {
        return struct;
    }

    public void setStruct(String struct) {
        this.struct = struct;
    }
    public String getUnion() {
        return union;
    }

    public void setUnion(String union) {
        this.union = union;
    }

    public myDsl_struct_or_union_specifier getMydsl_struct_or_union_specifier() {
        return mydsl_struct_or_union_specifier;
    }

    public void setMydsl_struct_or_union_specifier(myDsl_struct_or_union_specifier mydsl_struct_or_union_specifier) {
        this.mydsl_struct_or_union_specifier = mydsl_struct_or_union_specifier;
    }

}