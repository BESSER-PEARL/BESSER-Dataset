





import java.util.List;
import java.util.ArrayList;

public class HAL_BrevetType extends ReferenceBiblioType {

    private String page;
    private String datebrevet;
    private String pays;
    private String numbrevet;



    public HAL_BrevetType(
        String page,        String datebrevet,        String pays,        String numbrevet    ) {
        super(
        );
        this.page = page;
        this.datebrevet = datebrevet;
        this.pays = pays;
        this.numbrevet = numbrevet;
    }


    public String getPage() {
        return page;
    }

    public void setPage(String page) {
        this.page = page;
    }
    public String getDatebrevet() {
        return datebrevet;
    }

    public void setDatebrevet(String datebrevet) {
        this.datebrevet = datebrevet;
    }
    public String getPays() {
        return pays;
    }

    public void setPays(String pays) {
        this.pays = pays;
    }
    public String getNumbrevet() {
        return numbrevet;
    }

    public void setNumbrevet(String numbrevet) {
        this.numbrevet = numbrevet;
    }


}