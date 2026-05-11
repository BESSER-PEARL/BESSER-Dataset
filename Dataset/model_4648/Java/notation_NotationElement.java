





import java.util.List;
import java.util.ArrayList;

public class notation_NotationElement  {

    private String idBeforeRemoval;
    private String id;



    public notation_NotationElement(
        String idBeforeRemoval,        String id    ) {
        this.idBeforeRemoval = idBeforeRemoval;
        this.id = id;
    }


    public String getIdbeforeremoval() {
        return idBeforeRemoval;
    }

    public void setIdbeforeremoval(String idBeforeRemoval) {
        this.idBeforeRemoval = idBeforeRemoval;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}