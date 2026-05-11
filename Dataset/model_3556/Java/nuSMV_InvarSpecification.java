





import java.util.List;
import java.util.ArrayList;

public class nuSMV_InvarSpecification extends ModuleElement {

    private boolean semicolon;
    private String name;



    public nuSMV_InvarSpecification(
        boolean semicolon,        String name    ) {
        super(
        );
        this.semicolon = semicolon;
        this.name = name;
    }


    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}