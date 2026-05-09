





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_OperationalTransformation extends Module {






    private List<qvtoperational_Property> qvtoperational_propertys;




    private List<qvtoperational_Class> qvtoperational_classs;


    public qvtoperational_OperationalTransformation(
    ) {
        super(
        );
        this.qvtoperational_propertys = new ArrayList<>();
        this.qvtoperational_classs = new ArrayList<>();
    }

    public qvtoperational_OperationalTransformation(
        ArrayList<qvtoperational_Property> qvtoperational_propertys,        ArrayList<qvtoperational_Class> qvtoperational_classs    ) {
        this.qvtoperational_propertys = qvtoperational_propertys;
        this.qvtoperational_classs = qvtoperational_classs;
    }


    public List<qvtoperational_Property> getQvtoperational_propertys() {
        return qvtoperational_propertys;
    }

    public void addQvtoperational_property(Qvtoperational_property qvtoperational_property) {
        this.qvtoperational_propertys.add(qvtoperational_property);
    }
    public List<qvtoperational_Class> getQvtoperational_classs() {
        return qvtoperational_classs;
    }

    public void addQvtoperational_class(Qvtoperational_class qvtoperational_class) {
        this.qvtoperational_classs.add(qvtoperational_class);
    }

}