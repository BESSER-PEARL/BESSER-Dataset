





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_MOFRef  {

    private String id;





    private cvlmodel_StringToMOFRefMap cvlmodel_stringtomofrefmap;


    public cvlmodel_MOFRef(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public cvlmodel_StringToMOFRefMap getCvlmodel_stringtomofrefmap() {
        return cvlmodel_stringtomofrefmap;
    }

    public void setCvlmodel_stringtomofrefmap(cvlmodel_StringToMOFRefMap cvlmodel_stringtomofrefmap) {
        this.cvlmodel_stringtomofrefmap = cvlmodel_stringtomofrefmap;
    }

}