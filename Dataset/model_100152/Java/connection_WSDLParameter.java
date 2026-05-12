





import java.util.List;
import java.util.ArrayList;

public class connection_WSDLParameter  {

    private String ParameterInfoParent;
    private String Element;
    private String Expression;
    private String Column;
    private String source;
    private String ParameterInfo;





    private connection_WSDLSchemaConnection connection_wsdlschemaconnection;




    private connection_WSDLSchemaConnection connection_wsdlschemaconnection;


    public connection_WSDLParameter(
        String ParameterInfoParent,        String Element,        String Expression,        String Column,        String source,        String ParameterInfo    ) {
        this.ParameterInfoParent = ParameterInfoParent;
        this.Element = Element;
        this.Expression = Expression;
        this.Column = Column;
        this.source = source;
        this.ParameterInfo = ParameterInfo;
    }


    public String getParameterinfoparent() {
        return ParameterInfoParent;
    }

    public void setParameterinfoparent(String ParameterInfoParent) {
        this.ParameterInfoParent = ParameterInfoParent;
    }
    public String getElement() {
        return Element;
    }

    public void setElement(String Element) {
        this.Element = Element;
    }
    public String getExpression() {
        return Expression;
    }

    public void setExpression(String Expression) {
        this.Expression = Expression;
    }
    public String getColumn() {
        return Column;
    }

    public void setColumn(String Column) {
        this.Column = Column;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getParameterinfo() {
        return ParameterInfo;
    }

    public void setParameterinfo(String ParameterInfo) {
        this.ParameterInfo = ParameterInfo;
    }

    public connection_WSDLSchemaConnection getConnection_wsdlschemaconnection() {
        return connection_wsdlschemaconnection;
    }

    public void setConnection_wsdlschemaconnection(connection_WSDLSchemaConnection connection_wsdlschemaconnection) {
        this.connection_wsdlschemaconnection = connection_wsdlschemaconnection;
    }
    public connection_WSDLSchemaConnection getConnection_wsdlschemaconnection() {
        return connection_wsdlschemaconnection;
    }

    public void setConnection_wsdlschemaconnection(connection_WSDLSchemaConnection connection_wsdlschemaconnection) {
        this.connection_wsdlschemaconnection = connection_wsdlschemaconnection;
    }

}