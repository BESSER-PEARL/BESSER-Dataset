





import java.util.List;
import java.util.ArrayList;

public class sqlCrudGenerator_DataType  {

    private String dataType;
    private int precision;





    private sqlCrudGenerator_Column sqlcrudgenerator_column;


    public sqlCrudGenerator_DataType(
        String dataType,        int precision    ) {
        this.dataType = dataType;
        this.precision = precision;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }

    public sqlCrudGenerator_Column getSqlcrudgenerator_column() {
        return sqlcrudgenerator_column;
    }

    public void setSqlcrudgenerator_column(sqlCrudGenerator_Column sqlcrudgenerator_column) {
        this.sqlcrudgenerator_column = sqlcrudgenerator_column;
    }

}