





import java.util.List;
import java.util.ArrayList;

public class model_Room  {

    private String description;
    private String number;
    private String beds;
    private String clean;
    private String type;
    private String status;



    public model_Room(
        String description,        String number,        String beds,        String clean,        String type,        String status    ) {
        this.description = description;
        this.number = number;
        this.beds = beds;
        this.clean = clean;
        this.type = type;
        this.status = status;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getBeds() {
        return beds;
    }

    public void setBeds(String beds) {
        this.beds = beds;
    }
    public String getClean() {
        return clean;
    }

    public void setClean(String clean) {
        this.clean = clean;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}