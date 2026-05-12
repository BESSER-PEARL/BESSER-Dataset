





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Publisher  {

    private String name;
    private String address;





    private sistedesMM_Book sistedesmm_book;




    private sistedesMM_InProceedings sistedesmm_inproceedings;


    public sistedesMM_Publisher(
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

    public sistedesMM_Book getSistedesmm_book() {
        return sistedesmm_book;
    }

    public void setSistedesmm_book(sistedesMM_Book sistedesmm_book) {
        this.sistedesmm_book = sistedesmm_book;
    }
    public sistedesMM_InProceedings getSistedesmm_inproceedings() {
        return sistedesmm_inproceedings;
    }

    public void setSistedesmm_inproceedings(sistedesMM_InProceedings sistedesmm_inproceedings) {
        this.sistedesmm_inproceedings = sistedesmm_inproceedings;
    }

}