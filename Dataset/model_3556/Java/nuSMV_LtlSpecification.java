





import java.util.List;
import java.util.ArrayList;

public class nuSMV_LtlSpecification extends ModuleElement {

    private boolean nameId;
    private boolean semicolon;
    private String name;



    public nuSMV_LtlSpecification(
        boolean nameId,        boolean semicolon,        String name    ) {
        super(
        );
        this.nameId = nameId;
        this.semicolon = semicolon;
        this.name = name;
    }


    public boolean getNameid() {
        return nameId;
    }

    public void setNameid(boolean nameId) {
        this.nameId = nameId;
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