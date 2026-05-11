





import java.util.List;
import java.util.ArrayList;

public class lobj_Publisher  {

    private String id;
    private String publishername;





    private lobj_PublishInfo lobj_publishinfo;




    private lobj_Address lobj_address;


    public lobj_Publisher(
        String id,        String publishername    ) {
        this.id = id;
        this.publishername = publishername;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPublishername() {
        return publishername;
    }

    public void setPublishername(String publishername) {
        this.publishername = publishername;
    }

    public lobj_PublishInfo getLobj_publishinfo() {
        return lobj_publishinfo;
    }

    public void setLobj_publishinfo(lobj_PublishInfo lobj_publishinfo) {
        this.lobj_publishinfo = lobj_publishinfo;
    }
    public lobj_Address getLobj_address() {
        return lobj_address;
    }

    public void setLobj_address(lobj_Address lobj_address) {
        this.lobj_address = lobj_address;
    }

}