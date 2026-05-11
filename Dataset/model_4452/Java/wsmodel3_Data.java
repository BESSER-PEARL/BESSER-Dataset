





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_Data  {

    private String Date;
    private String Time;
    private String Location;
    private String Artefact;
    private String Attribute;
    private String id;



    public wsmodel3_Data(
        String Date,        String Time,        String Location,        String Artefact,        String Attribute,        String id    ) {
        this.Date = Date;
        this.Time = Time;
        this.Location = Location;
        this.Artefact = Artefact;
        this.Attribute = Attribute;
        this.id = id;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public String getArtefact() {
        return Artefact;
    }

    public void setArtefact(String Artefact) {
        this.Artefact = Artefact;
    }
    public String getAttribute() {
        return Attribute;
    }

    public void setAttribute(String Attribute) {
        this.Attribute = Attribute;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}