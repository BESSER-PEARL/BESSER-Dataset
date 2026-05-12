





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private int edition;
    private String acronym;
    private String name;
    private int id;
    private String attribute;



    public Event(
        int edition,        String acronym,        String name,        int id,        String attribute    ) {
        this.edition = edition;
        this.acronym = acronym;
        this.name = name;
        this.id = id;
        this.attribute = attribute;
    }


    public int getEdition() {
        return edition;
    }

    public void setEdition(int edition) {
        this.edition = edition;
    }
    public String getAcronym() {
        return acronym;
    }

    public void setAcronym(String acronym) {
        this.acronym = acronym;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}