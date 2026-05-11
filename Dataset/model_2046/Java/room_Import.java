





import java.util.List;
import java.util.ArrayList;

public class room_Import  {

    private String importedNamespace;
    private String importURI;





    private room_RoomModel room_roommodel;


    public room_Import(
        String importedNamespace,        String importURI    ) {
        this.importedNamespace = importedNamespace;
        this.importURI = importURI;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }
    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }

}