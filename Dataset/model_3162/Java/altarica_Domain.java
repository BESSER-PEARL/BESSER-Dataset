





import java.util.List;
import java.util.ArrayList;

public class altarica_Domain extends AbstractDeclaration {

    private String name;





    private altarica_AbstractDomain altarica_abstractdomain;


    public altarica_Domain(
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

    public altarica_AbstractDomain getAltarica_abstractdomain() {
        return altarica_abstractdomain;
    }

    public void setAltarica_abstractdomain(altarica_AbstractDomain altarica_abstractdomain) {
        this.altarica_abstractdomain = altarica_abstractdomain;
    }

}