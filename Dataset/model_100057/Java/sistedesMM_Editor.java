





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Editor  {

    private String name;





    private sistedesMM_InProceedings sistedesmm_inproceedings;


    public sistedesMM_Editor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sistedesMM_InProceedings getSistedesmm_inproceedings() {
        return sistedesmm_inproceedings;
    }

    public void setSistedesmm_inproceedings(sistedesMM_InProceedings sistedesmm_inproceedings) {
        this.sistedesmm_inproceedings = sistedesmm_inproceedings;
    }

}