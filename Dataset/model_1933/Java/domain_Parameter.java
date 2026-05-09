





import java.util.List;
import java.util.ArrayList;

public class domain_Parameter extends TypePointer {

    private String uid;
    private int order;
    private String name;



    public domain_Parameter(
        String uid,        int order,        String name    ) {
        super(
        );
        this.uid = uid;
        this.order = order;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}