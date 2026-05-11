





import java.util.List;
import java.util.ArrayList;

public class r1_Retrieve extends Expression {

    private String templateId;
    private String scope;
    private String codeProperty;
    private String dateProperty;
    private String idProperty;
    private String dataType;
    private String dateLowProperty;
    private String dateHighProperty;



    public r1_Retrieve(
        String templateId,        String scope,        String codeProperty,        String dateProperty,        String idProperty,        String dataType,        String dateLowProperty,        String dateHighProperty    ) {
        super(
        );
        this.templateId = templateId;
        this.scope = scope;
        this.codeProperty = codeProperty;
        this.dateProperty = dateProperty;
        this.idProperty = idProperty;
        this.dataType = dataType;
        this.dateLowProperty = dateLowProperty;
        this.dateHighProperty = dateHighProperty;
    }


    public String getTemplateid() {
        return templateId;
    }

    public void setTemplateid(String templateId) {
        this.templateId = templateId;
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
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getDatelowproperty() {
        return dateLowProperty;
    }

    public void setDatelowproperty(String dateLowProperty) {
        this.dateLowProperty = dateLowProperty;
    }
    public String getDatehighproperty() {
        return dateHighProperty;
    }

    public void setDatehighproperty(String dateHighProperty) {
        this.dateHighProperty = dateHighProperty;
    }


}