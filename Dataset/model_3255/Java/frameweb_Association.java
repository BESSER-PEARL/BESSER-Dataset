





import java.util.List;
import java.util.ArrayList;

public class frameweb_Association extends Relationship, Classifier {

    private String isDerived;





    private List<frameweb_Property> frameweb_propertys;




    private List<frameweb_Property> frameweb_propertys;




    private List<frameweb_Property> frameweb_propertys;




    private frameweb_Property frameweb_property;




    private frameweb_Property frameweb_property;


    public frameweb_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.frameweb_propertys = new ArrayList<>();
        this.frameweb_propertys = new ArrayList<>();
        this.frameweb_propertys = new ArrayList<>();
    }

    public frameweb_Association(
        String isDerived        ArrayList<frameweb_Property> frameweb_propertys,        ArrayList<frameweb_Property> frameweb_propertys,        ArrayList<frameweb_Property> frameweb_propertys    ) {
        this.isDerived = isDerived;
        this.frameweb_propertys = frameweb_propertys;
        this.frameweb_propertys = frameweb_propertys;
        this.frameweb_propertys = frameweb_propertys;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<frameweb_Property> getFrameweb_propertys() {
        return frameweb_propertys;
    }

    public void addFrameweb_property(Frameweb_property frameweb_property) {
        this.frameweb_propertys.add(frameweb_property);
    }
    public List<frameweb_Property> getFrameweb_propertys() {
        return frameweb_propertys;
    }

    public void addFrameweb_property(Frameweb_property frameweb_property) {
        this.frameweb_propertys.add(frameweb_property);
    }
    public List<frameweb_Property> getFrameweb_propertys() {
        return frameweb_propertys;
    }

    public void addFrameweb_property(Frameweb_property frameweb_property) {
        this.frameweb_propertys.add(frameweb_property);
    }
    public frameweb_Property getFrameweb_property() {
        return frameweb_property;
    }

    public void setFrameweb_property(frameweb_Property frameweb_property) {
        this.frameweb_property = frameweb_property;
    }
    public frameweb_Property getFrameweb_property() {
        return frameweb_property;
    }

    public void setFrameweb_property(frameweb_Property frameweb_property) {
        this.frameweb_property = frameweb_property;
    }

}