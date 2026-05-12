





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_routines_Routine extends SQLObject {

    private boolean deterministic;
    private String authorizationID;
    private String security;
    private String specificName;
    private String lastAlteredTS;
    private String parameterStyle;
    private String language;
    private String sqlDataAccess;
    private String externalName;
    private String creationTS;



    public sqlmodel_routines_Routine(
        boolean deterministic,        String authorizationID,        String security,        String specificName,        String lastAlteredTS,        String parameterStyle,        String language,        String sqlDataAccess,        String externalName,        String creationTS    ) {
        super(
        );
        this.deterministic = deterministic;
        this.authorizationID = authorizationID;
        this.security = security;
        this.specificName = specificName;
        this.lastAlteredTS = lastAlteredTS;
        this.parameterStyle = parameterStyle;
        this.language = language;
        this.sqlDataAccess = sqlDataAccess;
        this.externalName = externalName;
        this.creationTS = creationTS;
    }


    public boolean getDeterministic() {
        return deterministic;
    }

    public void setDeterministic(boolean deterministic) {
        this.deterministic = deterministic;
    }
    public String getAuthorizationid() {
        return authorizationID;
    }

    public void setAuthorizationid(String authorizationID) {
        this.authorizationID = authorizationID;
    }
    public String getSecurity() {
        return security;
    }

    public void setSecurity(String security) {
        this.security = security;
    }
    public String getSpecificname() {
        return specificName;
    }

    public void setSpecificname(String specificName) {
        this.specificName = specificName;
    }
    public String getLastalteredts() {
        return lastAlteredTS;
    }

    public void setLastalteredts(String lastAlteredTS) {
        this.lastAlteredTS = lastAlteredTS;
    }
    public String getParameterstyle() {
        return parameterStyle;
    }

    public void setParameterstyle(String parameterStyle) {
        this.parameterStyle = parameterStyle;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getSqldataaccess() {
        return sqlDataAccess;
    }

    public void setSqldataaccess(String sqlDataAccess) {
        this.sqlDataAccess = sqlDataAccess;
    }
    public String getExternalname() {
        return externalName;
    }

    public void setExternalname(String externalName) {
        this.externalName = externalName;
    }
    public String getCreationts() {
        return creationTS;
    }

    public void setCreationts(String creationTS) {
        this.creationTS = creationTS;
    }


}