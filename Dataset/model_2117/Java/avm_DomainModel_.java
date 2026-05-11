





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModel_  {

    private String Author;
    private String Notes;
    private String Name;
    private String XPosition;
    private String YPosition;





    private avm_Component avm_component;


    public avm_DomainModel_(
        String Author,        String Notes,        String Name,        String XPosition,        String YPosition    ) {
        this.Author = Author;
        this.Notes = Notes;
        this.Name = Name;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}