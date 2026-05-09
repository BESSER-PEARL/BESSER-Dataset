





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_Module extends Class, Package {

    private String isBlackbox;





    private List<Property> propertys;


    public QVTOperational_Module(
        String isBlackbox    ) {
        super(
        );
        this.isBlackbox = isBlackbox;
        this.propertys = new ArrayList<>();
    }

    public QVTOperational_Module(
        String isBlackbox        ArrayList<Property> propertys    ) {
        this.isBlackbox = isBlackbox;
        this.propertys = propertys;
    }

    public String getIsblackbox() {
        return isBlackbox;
    }

    public void setIsblackbox(String isBlackbox) {
        this.isBlackbox = isBlackbox;
    }

    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}