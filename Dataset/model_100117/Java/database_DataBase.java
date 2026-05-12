





import java.util.List;
import java.util.ArrayList;

public class database_DataBase extends TableContainer, TypesLibraryUser {

    private String url;





    private List<database_UserDefinedTypesLibrary> database_userdefinedtypeslibrarys;




    private List<database_Schema> database_schemas;


    public database_DataBase(
        String url    ) {
        super(
        );
        this.url = url;
        this.database_userdefinedtypeslibrarys = new ArrayList<>();
        this.database_schemas = new ArrayList<>();
    }

    public database_DataBase(
        String url        ArrayList<database_UserDefinedTypesLibrary> database_userdefinedtypeslibrarys,        ArrayList<database_Schema> database_schemas    ) {
        this.url = url;
        this.database_userdefinedtypeslibrarys = database_userdefinedtypeslibrarys;
        this.database_schemas = database_schemas;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public List<database_UserDefinedTypesLibrary> getDatabase_userdefinedtypeslibrarys() {
        return database_userdefinedtypeslibrarys;
    }

    public void addDatabase_userdefinedtypeslibrary(Database_userdefinedtypeslibrary database_userdefinedtypeslibrary) {
        this.database_userdefinedtypeslibrarys.add(database_userdefinedtypeslibrary);
    }
    public List<database_Schema> getDatabase_schemas() {
        return database_schemas;
    }

    public void addDatabase_schema(Database_schema database_schema) {
        this.database_schemas.add(database_schema);
    }

}