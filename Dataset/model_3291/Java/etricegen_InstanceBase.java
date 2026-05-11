





import java.util.List;
import java.util.ArrayList;

public class etricegen_InstanceBase  {

    private int threadId;
    private int objId;
    private String name;
    private String path;
    private int nObjIDs;



    public etricegen_InstanceBase(
        int threadId,        int objId,        String name,        String path,        int nObjIDs    ) {
        this.threadId = threadId;
        this.objId = objId;
        this.name = name;
        this.path = path;
        this.nObjIDs = nObjIDs;
    }


    public int getThreadid() {
        return threadId;
    }

    public void setThreadid(int threadId) {
        this.threadId = threadId;
    }
    public int getObjid() {
        return objId;
    }

    public void setObjid(int objId) {
        this.objId = objId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public int getNobjids() {
        return nObjIDs;
    }

    public void setNobjids(int nObjIDs) {
        this.nObjIDs = nObjIDs;
    }


}