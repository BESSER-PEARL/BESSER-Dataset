





import java.util.List;
import java.util.ArrayList;

public class astm_SpecificClassType extends ClassType {

    private String imports;
    private String package;



    public astm_SpecificClassType(
        String imports,        String package    ) {
        super(
        );
        this.imports = imports;
        this.package = package;
    }


    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }


}