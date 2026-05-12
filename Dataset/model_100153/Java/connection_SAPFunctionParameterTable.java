





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionParameterTable extends AbstractMetadataObject {






    private connection_SAPFunctionParameterColumn connection_sapfunctionparametercolumn;




    private List<connection_SAPFunctionParameterColumn> connection_sapfunctionparametercolumns;


    public connection_SAPFunctionParameterTable(
    ) {
        super(
        );
        this.connection_sapfunctionparametercolumns = new ArrayList<>();
    }

    public connection_SAPFunctionParameterTable(
        ArrayList<connection_SAPFunctionParameterColumn> connection_sapfunctionparametercolumns    ) {
        this.connection_sapfunctionparametercolumns = connection_sapfunctionparametercolumns;
    }


    public connection_SAPFunctionParameterColumn getConnection_sapfunctionparametercolumn() {
        return connection_sapfunctionparametercolumn;
    }

    public void setConnection_sapfunctionparametercolumn(connection_SAPFunctionParameterColumn connection_sapfunctionparametercolumn) {
        this.connection_sapfunctionparametercolumn = connection_sapfunctionparametercolumn;
    }
    public List<connection_SAPFunctionParameterColumn> getConnection_sapfunctionparametercolumns() {
        return connection_sapfunctionparametercolumns;
    }

    public void addConnection_sapfunctionparametercolumn(Connection_sapfunctionparametercolumn connection_sapfunctionparametercolumn) {
        this.connection_sapfunctionparametercolumns.add(connection_sapfunctionparametercolumn);
    }

}