





import java.util.List;
import java.util.ArrayList;

public class r1_Retrieve extends Expression {

    private String dateProperty;
    private String idProperty;
    private String templateId;
    private String dateLowProperty;
    private String codeProperty;
    private String dateHighProperty;
    private String dataType;
    private String scope;



    public r1_Retrieve(
        String dateProperty,        String idProperty,        String templateId,        String dateLowProperty,        String codeProperty,        String dateHighProperty,        String dataType,        String scope    ) {
        super(
        );
        this.dateProperty = dateProperty;
        this.idProperty = idProperty;
        this.templateId = templateId;
        this.dateLowProperty = dateLowProperty;
        this.codeProperty = codeProperty;
        this.dateHighProperty = dateHighProperty;
        this.dataType = dataType;
        this.scope = scope;
    }


    public String getDateproperty() {
        return dateProperty;
    }

    public void setDateproperty(String dateProperty) {
        this.dateProperty = dateProperty;
    }
    public String getIdproperty() {
        return idProperty;
    }

    public void setIdproperty(String idProperty) {
        this.idProperty = idProperty;
    }
    public String getTemplateid() {
        return templateId;
    }

    public void setTemplateid(String templateId) {
        this.templateId = templateId;
    }
    public String getDatelowproperty() {
        return dateLowProperty;
    }

    public void setDatelowproperty(String dateLowProperty) {
        this.dateLowProperty = dateLowProperty;
    }
    public String getCodeproperty() {
        return codeProperty;
    }

    public void setCodeproperty(String codeProperty) {
        this.codeProperty = codeProperty;
    }
    public String getDatehighproperty() {
        return dateHighProperty;
    }

    public void setDatehighproperty(String dateHighProperty) {
        this.dateHighProperty = dateHighProperty;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}