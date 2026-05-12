





import java.util.List;
import java.util.ArrayList;

public class plSql_ParameterDeclaration extends NameDeclaration {

    private String dataType;
    private String behavior;



    public plSql_ParameterDeclaration(
        String dataType,        String behavior    ) {
        super(
        );
        this.dataType = dataType;
        this.behavior = behavior;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }


}