





import java.util.List;
import java.util.ArrayList;

public class database_DataBase extends TypesLibraryUser, TableContainer {

    private String url;





    private List<database_UserDefinedTypesLibrary> database_userdefinedtypeslibrarys;


    public database_DataBase(
        String url    ) {
        super(
        );
        this.url = url;
        this.database_userdefinedtypeslibrarys = new ArrayList<>();
    }

    public database_DataBase(
        String url        ArrayList<database_UserDefinedTypesLibrary> database_userdefinedtypeslibrarys    ) {
        this.url = url;
        this.database_userdefinedtypeslibrarys = database_userdefinedtypeslibrarys;
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

}