





import java.util.List;
import java.util.ArrayList;

public class Schema  {






    private sqlmodel_tables_Trigger sqlmodel_tables_trigger;




    private sqlmodel_schema_Database sqlmodel_schema_database;




    private sqlmodel_accesscontrol_AuthorizationIdentifier sqlmodel_accesscontrol_authorizationidentifier;




    private sqlmodel_constraints_Index sqlmodel_constraints_index;




    private sqlmodel_schema_Catalog sqlmodel_schema_catalog;




    private sqlmodel_routines_Routine sqlmodel_routines_routine;




    private sqlmodel_datatypes_CharacterSet sqlmodel_datatypes_characterset;




    private sqlmodel_tables_Table sqlmodel_tables_table;


    public Schema(
    ) {
    }



    public sqlmodel_tables_Trigger getSqlmodel_tables_trigger() {
        return sqlmodel_tables_trigger;
    }

    public void setSqlmodel_tables_trigger(sqlmodel_tables_Trigger sqlmodel_tables_trigger) {
        this.sqlmodel_tables_trigger = sqlmodel_tables_trigger;
    }
    public sqlmodel_schema_Database getSqlmodel_schema_database() {
        return sqlmodel_schema_database;
    }

    public void setSqlmodel_schema_database(sqlmodel_schema_Database sqlmodel_schema_database) {
        this.sqlmodel_schema_database = sqlmodel_schema_database;
    }
    public sqlmodel_accesscontrol_AuthorizationIdentifier getSqlmodel_accesscontrol_authorizationidentifier() {
        return sqlmodel_accesscontrol_authorizationidentifier;
    }

    public void setSqlmodel_accesscontrol_authorizationidentifier(sqlmodel_accesscontrol_AuthorizationIdentifier sqlmodel_accesscontrol_authorizationidentifier) {
        this.sqlmodel_accesscontrol_authorizationidentifier = sqlmodel_accesscontrol_authorizationidentifier;
    }
    public sqlmodel_constraints_Index getSqlmodel_constraints_index() {
        return sqlmodel_constraints_index;
    }

    public void setSqlmodel_constraints_index(sqlmodel_constraints_Index sqlmodel_constraints_index) {
        this.sqlmodel_constraints_index = sqlmodel_constraints_index;
    }
    public sqlmodel_schema_Catalog getSqlmodel_schema_catalog() {
        return sqlmodel_schema_catalog;
    }

    public void setSqlmodel_schema_catalog(sqlmodel_schema_Catalog sqlmodel_schema_catalog) {
        this.sqlmodel_schema_catalog = sqlmodel_schema_catalog;
    }
    public sqlmodel_routines_Routine getSqlmodel_routines_routine() {
        return sqlmodel_routines_routine;
    }

    public void setSqlmodel_routines_routine(sqlmodel_routines_Routine sqlmodel_routines_routine) {
        this.sqlmodel_routines_routine = sqlmodel_routines_routine;
    }
    public sqlmodel_datatypes_CharacterSet getSqlmodel_datatypes_characterset() {
        return sqlmodel_datatypes_characterset;
    }

    public void setSqlmodel_datatypes_characterset(sqlmodel_datatypes_CharacterSet sqlmodel_datatypes_characterset) {
        this.sqlmodel_datatypes_characterset = sqlmodel_datatypes_characterset;
    }
    public sqlmodel_tables_Table getSqlmodel_tables_table() {
        return sqlmodel_tables_table;
    }

    public void setSqlmodel_tables_table(sqlmodel_tables_Table sqlmodel_tables_table) {
        this.sqlmodel_tables_table = sqlmodel_tables_table;
    }

}