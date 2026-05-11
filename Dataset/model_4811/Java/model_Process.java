





import java.util.List;
import java.util.ArrayList;

public class model_Process extends BPELExtensibleElement {

    private String exitOnStandardFault;
    private String targetNamespace;
    private String name;
    private String abstractProcessProfile;
    private String expressionLanguage;
    private String variableAccessSerializable;
    private String queryLanguage;
    private String suppressJoinFailure;



    public model_Process(
        String exitOnStandardFault,        String targetNamespace,        String name,        String abstractProcessProfile,        String expressionLanguage,        String variableAccessSerializable,        String queryLanguage,        String suppressJoinFailure    ) {
        super(
        );
        this.exitOnStandardFault = exitOnStandardFault;
        this.targetNamespace = targetNamespace;
        this.name = name;
        this.abstractProcessProfile = abstractProcessProfile;
        this.expressionLanguage = expressionLanguage;
        this.variableAccessSerializable = variableAccessSerializable;
        this.queryLanguage = queryLanguage;
        this.suppressJoinFailure = suppressJoinFailure;
    }


    public String getExitonstandardfault() {
        return exitOnStandardFault;
    }

    public void setExitonstandardfault(String exitOnStandardFault) {
        this.exitOnStandardFault = exitOnStandardFault;
    }
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAbstractprocessprofile() {
        return abstractProcessProfile;
    }

    public void setAbstractprocessprofile(String abstractProcessProfile) {
        this.abstractProcessProfile = abstractProcessProfile;
    }
    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public String getVariableaccessserializable() {
        return variableAccessSerializable;
    }

    public void setVariableaccessserializable(String variableAccessSerializable) {
        this.variableAccessSerializable = variableAccessSerializable;
    }
    public String getQuerylanguage() {
        return queryLanguage;
    }

    public void setQuerylanguage(String queryLanguage) {
        this.queryLanguage = queryLanguage;
    }
    public String getSuppressjoinfailure() {
        return suppressJoinFailure;
    }

    public void setSuppressjoinfailure(String suppressJoinFailure) {
        this.suppressJoinFailure = suppressJoinFailure;
    }


}