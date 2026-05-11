





import java.util.List;
import java.util.ArrayList;

public class webapp_Attribute extends Named {

    private String type;





    private List<webapp_DataStructure> webapp_datastructures;




    private webapp_DataStructure webapp_datastructure;




    private webapp_DataStructure webapp_datastructure;




    private webapp_DataStructure webapp_datastructure;


    public webapp_Attribute(
        String type    ) {
        super(
        );
        this.type = type;
        this.webapp_datastructures = new ArrayList<>();
    }

    public webapp_Attribute(
        String type        ArrayList<webapp_DataStructure> webapp_datastructures    ) {
        this.type = type;
        this.webapp_datastructures = webapp_datastructures;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<webapp_DataStructure> getWebapp_datastructures() {
        return webapp_datastructures;
    }

    public void addWebapp_datastructure(Webapp_datastructure webapp_datastructure) {
        this.webapp_datastructures.add(webapp_datastructure);
    }
    public webapp_DataStructure getWebapp_datastructure() {
        return webapp_datastructure;
    }

    public void setWebapp_datastructure(webapp_DataStructure webapp_datastructure) {
        this.webapp_datastructure = webapp_datastructure;
    }
    public webapp_DataStructure getWebapp_datastructure() {
        return webapp_datastructure;
    }

    public void setWebapp_datastructure(webapp_DataStructure webapp_datastructure) {
        this.webapp_datastructure = webapp_datastructure;
    }
    public webapp_DataStructure getWebapp_datastructure() {
        return webapp_datastructure;
    }

    public void setWebapp_datastructure(webapp_DataStructure webapp_datastructure) {
        this.webapp_datastructure = webapp_datastructure;
    }

}