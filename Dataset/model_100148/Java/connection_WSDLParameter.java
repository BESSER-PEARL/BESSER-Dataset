





import java.util.List;
import java.util.ArrayList;

public class connection_WSDLParameter  {

    private String ParameterInfoParent;
    private String ParameterInfo;
    private String Expression;
    private String Column;
    private String Element;
    private String source;





    private connection_WSDLSchemaConnection connection_wsdlschemaconnection;




    private connection_WSDLSchemaConnection connection_wsdlschemaconnection;


    public connection_WSDLParameter(
        String ParameterInfoParent,        String ParameterInfo,        String Expression,        String Column,        String Element,        String source    ) {
        this.ParameterInfoParent = ParameterInfoParent;
        this.ParameterInfo = ParameterInfo;
        this.Expression = Expression;
        this.Column = Column;
        this.Element = Element;
        this.source = source;
    }


    public String getParameterinfoparent() {
        return ParameterInfoParent;
    }

    public void setParameterinfoparent(String ParameterInfoParent) {
        this.ParameterInfoParent = ParameterInfoParent;
    }
    public String getParameterinfo() {
        return ParameterInfo;
    }

    public void setParameterinfo(String ParameterInfo) {
        this.ParameterInfo = ParameterInfo;
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
    public String getElement() {
        return Element;
    }

    public void setElement(String Element) {
        this.Element = Element;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
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