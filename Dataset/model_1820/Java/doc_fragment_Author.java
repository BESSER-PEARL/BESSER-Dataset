





import java.util.List;
import java.util.ArrayList;

public class doc_fragment_Author  {

    private String id;
    private String ref;
    private String name;



    public doc_fragment_Author(
        String id,        String ref,        String name    ) {
        this.id = id;
        this.ref = ref;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}