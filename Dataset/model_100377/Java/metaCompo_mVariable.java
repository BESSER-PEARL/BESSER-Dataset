





import java.util.List;
import java.util.ArrayList;

public class metaCompo_mVariable  {

    private String name;
    private String type;





    private metaCompo_mPort metacompo_mport;




    private metaCompo_mFSM metacompo_mfsm;


    public metaCompo_mVariable(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public metaCompo_mPort getMetacompo_mport() {
        return metacompo_mport;
    }

    public void setMetacompo_mport(metaCompo_mPort metacompo_mport) {
        this.metacompo_mport = metacompo_mport;
    }
    public metaCompo_mFSM getMetacompo_mfsm() {
        return metacompo_mfsm;
    }

    public void setMetacompo_mfsm(metaCompo_mFSM metacompo_mfsm) {
        this.metacompo_mfsm = metacompo_mfsm;
    }

}