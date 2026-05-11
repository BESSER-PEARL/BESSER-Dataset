





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModel_  {

    private String Name;
    private String YPosition;
    private String XPosition;
    private String ID;
    private String Author;
    private String Notes;





    private avm_Component avm_component;




    private avm_Container avm_container;




    private avm_TestBench avm_testbench;


    public avm_DomainModel_(
        String Name,        String YPosition,        String XPosition,        String ID,        String Author,        String Notes    ) {
        this.Name = Name;
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.ID = ID;
        this.Author = Author;
        this.Notes = Notes;
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
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
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

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }
    public avm_Container getAvm_container() {
        return avm_container;
    }

    public void setAvm_container(avm_Container avm_container) {
        this.avm_container = avm_container;
    }
    public avm_TestBench getAvm_testbench() {
        return avm_testbench;
    }

    public void setAvm_testbench(avm_TestBench avm_testbench) {
        this.avm_testbench = avm_testbench;
    }

}