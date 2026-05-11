





import java.util.List;
import java.util.ArrayList;

public class wh_PackageDeclaration extends AbstractElement {

    private String name;



    public wh_PackageDeclaration(
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