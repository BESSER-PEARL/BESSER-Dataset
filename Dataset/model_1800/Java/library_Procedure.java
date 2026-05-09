





import java.util.List;
import java.util.ArrayList;

public class library_Procedure  {

    private String name;





    private List<library_Message> library_messages;




    private library_Protocol library_protocol;


    public library_Procedure(
        String name    ) {
        this.name = name;
        this.library_messages = new ArrayList<>();
    }

    public library_Procedure(
        String name        ArrayList<library_Message> library_messages    ) {
        this.name = name;
        this.library_messages = library_messages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_Message> getLibrary_messages() {
        return library_messages;
    }

    public void addLibrary_message(Library_message library_message) {
        this.library_messages.add(library_message);
    }
    public library_Protocol getLibrary_protocol() {
        return library_protocol;
    }

    public void setLibrary_protocol(library_Protocol library_protocol) {
        this.library_protocol = library_protocol;
    }

}