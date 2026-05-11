





import java.util.List;
import java.util.ArrayList;

public class notation_NotationElement  {

    private String id;
    private String idBeforeRemoval;



    public notation_NotationElement(
        String id,        String idBeforeRemoval    ) {
        this.id = id;
        this.idBeforeRemoval = idBeforeRemoval;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getIdbeforeremoval() {
        return idBeforeRemoval;
    }

    public void setIdbeforeremoval(String idBeforeRemoval) {
        this.idBeforeRemoval = idBeforeRemoval;
    }


}