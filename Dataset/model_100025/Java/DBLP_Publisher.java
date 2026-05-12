





import java.util.List;
import java.util.ArrayList;

public class DBLP_Publisher  {

    private String name;
    private String address;





    private DBLP_Proceedings dblp_proceedings;




    private DBLP_InCollection dblp_incollection;




    private DBLP_Book dblp_book;




    private DBLP_InProceedings dblp_inproceedings;


    public DBLP_Publisher(
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
    public DBLP_Book getDblp_book() {
        return dblp_book;
    }

    public void setDblp_book(DBLP_Book dblp_book) {
        this.dblp_book = dblp_book;
    }
    public DBLP_InProceedings getDblp_inproceedings() {
        return dblp_inproceedings;
    }

    public void setDblp_inproceedings(DBLP_InProceedings dblp_inproceedings) {
        this.dblp_inproceedings = dblp_inproceedings;
    }

}