





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_Table extends NamedColumnSet {

    private String isTemporary;
    private String isSystem;
    private String temporaryScope;



    public CWMRelationalData_Table(
        String isTemporary,        String isSystem,        String temporaryScope    ) {
        super(
        );
        this.isTemporary = isTemporary;
        this.isSystem = isSystem;
        this.temporaryScope = temporaryScope;
    }


    public String getIstemporary() {
        return isTemporary;
    }

    public void setIstemporary(String isTemporary) {
        this.isTemporary = isTemporary;
    }
    public String getIssystem() {
        return isSystem;
    }

    public void setIssystem(String isSystem) {
        this.isSystem = isSystem;
    }
    public String getTemporaryscope() {
        return temporaryScope;
    }

    public void setTemporaryscope(String temporaryScope) {
        this.temporaryScope = temporaryScope;
    }


}