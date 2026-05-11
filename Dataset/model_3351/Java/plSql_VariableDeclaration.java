





import java.util.List;
import java.util.ArrayList;

public class plSql_VariableDeclaration extends ItemDeclaration, NameDeclaration {

    private String dataType;
    private boolean isNotNull;
    private boolean isConstant;



    public plSql_VariableDeclaration(
        String dataType,        boolean isNotNull,        boolean isConstant    ) {
        super(
        );
        this.dataType = dataType;
        this.isNotNull = isNotNull;
        this.isConstant = isConstant;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public boolean getIsnotnull() {
        return isNotNull;
    }

    public void setIsnotnull(boolean isNotNull) {
        this.isNotNull = isNotNull;
    }
    public boolean getIsconstant() {
        return isConstant;
    }

    public void setIsconstant(boolean isConstant) {
        this.isConstant = isConstant;
    }


}