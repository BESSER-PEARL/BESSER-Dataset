





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModel  {

    private String ID;
    private String Notes;
    private String XPosition;
    private String Name;
    private String YPosition;
    private String Author;





    private List<avm_Resource> avm_resources;




    private avm_Component avm_component;


    public avm_DomainModel(
        String ID,        String Notes,        String XPosition,        String Name,        String YPosition,        String Author    ) {
        this.ID = ID;
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.Name = Name;
        this.YPosition = YPosition;
        this.Author = Author;
        this.avm_resources = new ArrayList<>();
    }

    public avm_DomainModel(
        String ID,        String Notes,        String XPosition,        String Name,        String YPosition,        String Author        ArrayList<avm_Resource> avm_resources    ) {
        this.ID = ID;
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.Name = Name;
        this.YPosition = YPosition;
        this.Author = Author;
        this.avm_resources = avm_resources;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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

    public List<avm_Resource> getAvm_resources() {
        return avm_resources;
    }

    public void addAvm_resource(Avm_resource avm_resource) {
        this.avm_resources.add(avm_resource);
    }
    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}