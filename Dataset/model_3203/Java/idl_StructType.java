





import java.util.List;
import java.util.ArrayList;

public class idl_StructType extends ConstrTypeSpec, TypeDecl, Definition {

    private String name;



    public idl_StructType(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}