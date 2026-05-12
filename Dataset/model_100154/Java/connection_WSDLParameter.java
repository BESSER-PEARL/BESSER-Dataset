





import java.util.List;
import java.util.ArrayList;

public class connection_WSDLParameter  {

    private String Element;
    private String ParameterInfo;
    private String Column;
    private String source;
    private String ParameterInfoParent;
    private String Expression;





    private connection_WSDLSchemaConnection connection_wsdlschemaconnection;




    private connection_WSDLSchemaConnection connection_wsdlschemaconnection;


    public connection_WSDLParameter(
        String Element,        String ParameterInfo,        String Column,        String source,        String ParameterInfoParent,        String Expression    ) {
        this.Element = Element;
        this.ParameterInfo = ParameterInfo;
        this.Column = Column;
        this.source = source;
        this.ParameterInfoParent = ParameterInfoParent;
        this.Expression = Expression;
    }


    public String getElement() {
        return Element;
    }

    public void setElement(String Element) {
        this.Element = Element;
    }
    public String getParameterinfo() {
        return ParameterInfo;
    }

    public void setParameterinfo(String ParameterInfo) {
        this.ParameterInfo = ParameterInfo;
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
    public String getParameterinfoparent() {
        return ParameterInfoParent;
    }

    public void setParameterinfoparent(String ParameterInfoParent) {
        this.ParameterInfoParent = ParameterInfoParent;
    }
    public String getExpression() {
        return Expression;
    }

    public void setExpression(String Expression) {
        this.Expression = Expression;
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