





import java.util.List;
import java.util.ArrayList;

public class di_DiagramElement  {

    private String anyAttribute;
    private String id;





    private di_Plane di_plane;


    public di_DiagramElement(
        String anyAttribute,        String id    ) {
        this.anyAttribute = anyAttribute;
        this.id = id;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public di_Plane getDi_plane() {
        return di_plane;
    }

    public void setDi_plane(di_Plane di_plane) {
        this.di_plane = di_plane;
    }

}