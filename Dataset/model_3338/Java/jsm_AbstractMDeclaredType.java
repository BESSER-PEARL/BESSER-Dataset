





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractMDeclaredType extends AbstractMTypeContainer {

    private String name;



    public jsm_AbstractMDeclaredType(
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