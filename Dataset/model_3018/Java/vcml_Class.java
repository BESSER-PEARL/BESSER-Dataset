





import java.util.List;
import java.util.ArrayList;

public class vcml_Class extends VCObject {

    private String status;
    private String group;





    private List<vcml_Class> vcml_classs;


    public vcml_Class(
        String status,        String group    ) {
        super(
        );
        this.status = status;
        this.group = group;
        this.vcml_classs = new ArrayList<>();
    }

    public vcml_Class(
        String status,        String group        ArrayList<vcml_Class> vcml_classs    ) {
        this.status = status;
        this.group = group;
        this.vcml_classs = vcml_classs;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<vcml_Class> getVcml_classs() {
        return vcml_classs;
    }

    public void addVcml_class(Vcml_class vcml_class) {
        this.vcml_classs.add(vcml_class);
    }

}