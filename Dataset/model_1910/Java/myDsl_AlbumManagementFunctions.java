





import java.util.List;
import java.util.ArrayList;

public class myDsl_AlbumManagementFunctions  {

    private String name;





    private myDsl_AlbumManagement mydsl_albummanagement;


    public myDsl_AlbumManagementFunctions(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_AlbumManagement getMydsl_albummanagement() {
        return mydsl_albummanagement;
    }

    public void setMydsl_albummanagement(myDsl_AlbumManagement mydsl_albummanagement) {
        this.mydsl_albummanagement = mydsl_albummanagement;
    }

}