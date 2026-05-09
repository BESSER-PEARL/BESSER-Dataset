





import java.util.List;
import java.util.ArrayList;

public class jbatch_Split  {

    private String id;
    private String next;



    public jbatch_Split(
        String id,        String next    ) {
        this.id = id;
        this.next = next;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNext() {
        return next;
    }

    public void setNext(String next) {
        this.next = next;
    }


}