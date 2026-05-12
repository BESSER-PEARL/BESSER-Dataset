





import java.util.List;
import java.util.ArrayList;

public class DBLP_School  {

    private String name;
    private String address;





    private DBLP_PhDThesis dblp_phdthesis;




    private DBLP_MastersThesis dblp_mastersthesis;


    public DBLP_School(
        String name,        String address    ) {
        this.name = name;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public DBLP_PhDThesis getDblp_phdthesis() {
        return dblp_phdthesis;
    }

    public void setDblp_phdthesis(DBLP_PhDThesis dblp_phdthesis) {
        this.dblp_phdthesis = dblp_phdthesis;
    }
    public DBLP_MastersThesis getDblp_mastersthesis() {
        return dblp_mastersthesis;
    }

    public void setDblp_mastersthesis(DBLP_MastersThesis dblp_mastersthesis) {
        this.dblp_mastersthesis = dblp_mastersthesis;
    }

}