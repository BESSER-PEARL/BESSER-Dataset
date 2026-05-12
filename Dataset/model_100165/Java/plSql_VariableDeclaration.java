





import java.util.List;
import java.util.ArrayList;

public class plSql_VariableDeclaration extends ItemDeclaration, NameDeclaration {

    private boolean isNotNull;
    private String dataType;
    private boolean isConstant;



    public plSql_VariableDeclaration(
        boolean isNotNull,        String dataType,        boolean isConstant    ) {
        super(
        );
        this.isNotNull = isNotNull;
        this.dataType = dataType;
        this.isConstant = isConstant;
    }


    public boolean getIsnotnull() {
        return isNotNull;
    }

    public void setIsnotnull(boolean isNotNull) {
        this.isNotNull = isNotNull;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public boolean getIsconstant() {
        return isConstant;
    }

    public void setIsconstant(boolean isConstant) {
        this.isConstant = isConstant;
    }


}