





import java.util.List;
import java.util.ArrayList;

public class Database  {






    private sqlmodel_schema_Event sqlmodel_schema_event;




    private sqlmodel_schema_Catalog sqlmodel_schema_catalog;




    private sqlmodel_accesscontrol_AuthorizationIdentifier sqlmodel_accesscontrol_authorizationidentifier;




    private sqlmodel_schema_Schema sqlmodel_schema_schema;


    public Database(
    ) {
    }



    public sqlmodel_schema_Event getSqlmodel_schema_event() {
        return sqlmodel_schema_event;
    }

    public void setSqlmodel_schema_event(sqlmodel_schema_Event sqlmodel_schema_event) {
        this.sqlmodel_schema_event = sqlmodel_schema_event;
    }
    public sqlmodel_schema_Catalog getSqlmodel_schema_catalog() {
        return sqlmodel_schema_catalog;
    }

    public void setSqlmodel_schema_catalog(sqlmodel_schema_Catalog sqlmodel_schema_catalog) {
        this.sqlmodel_schema_catalog = sqlmodel_schema_catalog;
    }
    public sqlmodel_accesscontrol_AuthorizationIdentifier getSqlmodel_accesscontrol_authorizationidentifier() {
        return sqlmodel_accesscontrol_authorizationidentifier;
    }

    public void setSqlmodel_accesscontrol_authorizationidentifier(sqlmodel_accesscontrol_AuthorizationIdentifier sqlmodel_accesscontrol_authorizationidentifier) {
        this.sqlmodel_accesscontrol_authorizationidentifier = sqlmodel_accesscontrol_authorizationidentifier;
    }
    public sqlmodel_schema_Schema getSqlmodel_schema_schema() {
        return sqlmodel_schema_schema;
    }

    public void setSqlmodel_schema_schema(sqlmodel_schema_Schema sqlmodel_schema_schema) {
        this.sqlmodel_schema_schema = sqlmodel_schema_schema;
    }

}