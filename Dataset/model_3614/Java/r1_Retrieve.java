





import java.util.List;
import java.util.ArrayList;

public class r1_Retrieve extends Expression {

    private String dateLowProperty;
    private String dataType;
    private String dateProperty;
    private String dateHighProperty;
    private String scope;
    private String codeProperty;
    private String templateId;
    private String idProperty;



    public r1_Retrieve(
        String dateLowProperty,        String dataType,        String dateProperty,        String dateHighProperty,        String scope,        String codeProperty,        String templateId,        String idProperty    ) {
        super(
        );
        this.dateLowProperty = dateLowProperty;
        this.dataType = dataType;
        this.dateProperty = dateProperty;
        this.dateHighProperty = dateHighProperty;
        this.scope = scope;
        this.codeProperty = codeProperty;
        this.templateId = templateId;
        this.idProperty = idProperty;
    }


    public String getDatelowproperty() {
        return dateLowProperty;
    }

    public void setDatelowproperty(String dateLowProperty) {
        this.dateLowProperty = dateLowProperty;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getDateproperty() {
        return dateProperty;
    }

    public void setDateproperty(String dateProperty) {
        this.dateProperty = dateProperty;
    }
    public String getDatehighproperty() {
        return dateHighProperty;
    }

    public void setDatehighproperty(String dateHighProperty) {
        this.dateHighProperty = dateHighProperty;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getCodeproperty() {
        return codeProperty;
    }

    public void setCodeproperty(String codeProperty) {
        this.codeProperty = codeProperty;
    }
    public String getTemplateid() {
        return templateId;
    }

    public void setTemplateid(String templateId) {
        this.templateId = templateId;
    }
    public String getIdproperty() {
        return idProperty;
    }

    public void setIdproperty(String idProperty) {
        this.idProperty = idProperty;
    }


}