





import java.util.List;
import java.util.ArrayList;

public class DBLP_Editor  {

    private String name;





    private DBLP_Www dblp_www;




    private DBLP_Proceedings dblp_proceedings;




    private DBLP_InCollection dblp_incollection;




    private DBLP_InProceedings dblp_inproceedings;


    public DBLP_Editor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DBLP_Www getDblp_www() {
        return dblp_www;
    }

    public void setDblp_www(DBLP_Www dblp_www) {
        this.dblp_www = dblp_www;
    }
    public DBLP_Proceedings getDblp_proceedings() {
        return dblp_proceedings;
    }

    public void setDblp_proceedings(DBLP_Proceedings dblp_proceedings) {
        this.dblp_proceedings = dblp_proceedings;
    }
    public DBLP_InCollection getDblp_incollection() {
        return dblp_incollection;
    }

    public void setDblp_incollection(DBLP_InCollection dblp_incollection) {
        this.dblp_incollection = dblp_incollection;
    }
    public DBLP_InProceedings getDblp_inproceedings() {
        return dblp_inproceedings;
    }

    public void setDblp_inproceedings(DBLP_InProceedings dblp_inproceedings) {
        this.dblp_inproceedings = dblp_inproceedings;
    }

}