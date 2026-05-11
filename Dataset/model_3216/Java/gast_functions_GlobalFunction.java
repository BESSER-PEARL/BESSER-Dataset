





import java.util.List;
import java.util.ArrayList;

public class gast_functions_GlobalFunction extends Function {

    private String kind;





    private Package package;


    public gast_functions_GlobalFunction(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }

}