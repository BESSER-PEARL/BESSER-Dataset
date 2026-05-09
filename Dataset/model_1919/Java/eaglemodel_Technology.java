





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Technology  {

    private String name;





    private List<eaglemodel_Attribute> eaglemodel_attributes;




    private eaglemodel_Technologies eaglemodel_technologies;


    public eaglemodel_Technology(
        String name    ) {
        this.name = name;
        this.eaglemodel_attributes = new ArrayList<>();
    }

    public eaglemodel_Technology(
        String name        ArrayList<eaglemodel_Attribute> eaglemodel_attributes    ) {
        this.name = name;
        this.eaglemodel_attributes = eaglemodel_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eaglemodel_Attribute> getEaglemodel_attributes() {
        return eaglemodel_attributes;
    }

    public void addEaglemodel_attribute(Eaglemodel_attribute eaglemodel_attribute) {
        this.eaglemodel_attributes.add(eaglemodel_attribute);
    }
    public eaglemodel_Technologies getEaglemodel_technologies() {
        return eaglemodel_technologies;
    }

    public void setEaglemodel_technologies(eaglemodel_Technologies eaglemodel_technologies) {
        this.eaglemodel_technologies = eaglemodel_technologies;
    }

}