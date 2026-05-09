





import java.util.List;
import java.util.ArrayList;

public class PagosPim_TerminalValue extends Expression {

    private String value;
    private String method;





    private PagosPim_LogicalExpression pagospim_logicalexpression;




    private PagosPim_LogicalExpression pagospim_logicalexpression;




    private PagosPim_EObject pagospim_eobject;




    private PagosPim_Attribute pagospim_attribute;


    public PagosPim_TerminalValue(
        String value,        String method    ) {
        super(
        );
        this.value = value;
        this.method = method;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public PagosPim_LogicalExpression getPagospim_logicalexpression() {
        return pagospim_logicalexpression;
    }

    public void setPagospim_logicalexpression(PagosPim_LogicalExpression pagospim_logicalexpression) {
        this.pagospim_logicalexpression = pagospim_logicalexpression;
    }
    public PagosPim_LogicalExpression getPagospim_logicalexpression() {
        return pagospim_logicalexpression;
    }

    public void setPagospim_logicalexpression(PagosPim_LogicalExpression pagospim_logicalexpression) {
        this.pagospim_logicalexpression = pagospim_logicalexpression;
    }
    public PagosPim_EObject getPagospim_eobject() {
        return pagospim_eobject;
    }

    public void setPagospim_eobject(PagosPim_EObject pagospim_eobject) {
        this.pagospim_eobject = pagospim_eobject;
    }
    public PagosPim_Attribute getPagospim_attribute() {
        return pagospim_attribute;
    }

    public void setPagospim_attribute(PagosPim_Attribute pagospim_attribute) {
        this.pagospim_attribute = pagospim_attribute;
    }

}