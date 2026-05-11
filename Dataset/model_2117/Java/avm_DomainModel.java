





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModel  {

    private String Name;
    private String Author;
    private String Notes;
    private String YPosition;
    private String XPosition;





    private avm_Component avm_component;


    public avm_DomainModel(
        String Name,        String Author,        String Notes,        String YPosition,        String XPosition    ) {
        this.Name = Name;
        this.Author = Author;
        this.Notes = Notes;
        this.YPosition = YPosition;
        this.XPosition = XPosition;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAuthor() {
        return Author;
    }

    public void setAuthor(String Author) {
        this.Author = Author;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}