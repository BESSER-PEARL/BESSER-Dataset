





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModel  {

    private String ID;
    private String Notes;
    private String XPosition;
    private String YPosition;
    private String Author;
    private String Name;





    private avm_Component avm_component;


    public avm_DomainModel(
        String ID,        String Notes,        String XPosition,        String YPosition,        String Author,        String Name    ) {
        this.ID = ID;
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
        this.Author = Author;
        this.Name = Name;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getAuthor() {
        return Author;
    }

    public void setAuthor(String Author) {
        this.Author = Author;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}