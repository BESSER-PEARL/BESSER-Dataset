





import java.util.List;
import java.util.ArrayList;

public class database_DataBase extends TypesLibraryUser, TableContainer {

    private String url;



    public database_DataBase(
        String url    ) {
        super(
        );
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}