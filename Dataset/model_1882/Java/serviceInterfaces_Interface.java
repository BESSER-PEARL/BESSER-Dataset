





import java.util.List;
import java.util.ArrayList;

public class serviceInterfaces_Interface extends Packageable {

    private String qName;
    private String description;



    public serviceInterfaces_Interface(
        String qName,        String description    ) {
        super(
        );
        this.qName = qName;
        this.description = description;
    }


    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}