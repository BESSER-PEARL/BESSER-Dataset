





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_Module extends Class {

    private String isBlackbox;





    private List<qvtoperational_Property> qvtoperational_propertys;


    public qvtoperational_Module(
        String isBlackbox    ) {
        super(
        );
        this.isBlackbox = isBlackbox;
        this.qvtoperational_propertys = new ArrayList<>();
    }

    public qvtoperational_Module(
        String isBlackbox        ArrayList<qvtoperational_Property> qvtoperational_propertys    ) {
        this.isBlackbox = isBlackbox;
        this.qvtoperational_propertys = qvtoperational_propertys;
    }

    public String getIsblackbox() {
        return isBlackbox;
    }

    public void setIsblackbox(String isBlackbox) {
        this.isBlackbox = isBlackbox;
    }

    public List<qvtoperational_Property> getQvtoperational_propertys() {
        return qvtoperational_propertys;
    }

    public void addQvtoperational_property(Qvtoperational_property qvtoperational_property) {
        this.qvtoperational_propertys.add(qvtoperational_property);
    }

}