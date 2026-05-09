





import java.util.List;
import java.util.ArrayList;

public class domain_Dependency  {

    private String name;
    private String uid;





    private domain_DataControl domain_datacontrol;




    private domain_Controls domain_controls;




    private domain_DataControl domain_datacontrol;


    public domain_Dependency(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_DataControl getDomain_datacontrol() {
        return domain_datacontrol;
    }

    public void setDomain_datacontrol(domain_DataControl domain_datacontrol) {
        this.domain_datacontrol = domain_datacontrol;
    }
    public domain_Controls getDomain_controls() {
        return domain_controls;
    }

    public void setDomain_controls(domain_Controls domain_controls) {
        this.domain_controls = domain_controls;
    }
    public domain_DataControl getDomain_datacontrol() {
        return domain_datacontrol;
    }

    public void setDomain_datacontrol(domain_DataControl domain_datacontrol) {
        this.domain_datacontrol = domain_datacontrol;
    }

}