





import java.util.List;
import java.util.ArrayList;

public class metaCompo_mPort  {

    private String type;
    private String name;
    private String io;





    private metaCompo_mPort metacompo_mport;


    public metaCompo_mPort(
        String type,        String name,        String io    ) {
        this.type = type;
        this.name = name;
        this.io = io;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIo() {
        return io;
    }

    public void setIo(String io) {
        this.io = io;
    }

    public metaCompo_mPort getMetacompo_mport() {
        return metacompo_mport;
    }

    public void setMetacompo_mport(metaCompo_mPort metacompo_mport) {
        this.metacompo_mport = metacompo_mport;
    }

}