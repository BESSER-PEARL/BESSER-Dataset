




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class zlvp_Essen  {

    private int id;
    private String nacht;
    private LocalDate datum;
    private String vormittag;
    private String nachmittag;





    private zlvp_Lager zlvp_lager;


    public zlvp_Essen(
        int id,        String nacht,        LocalDate datum,        String vormittag,        String nachmittag    ) {
        this.id = id;
        this.nacht = nacht;
        this.datum = datum;
        this.vormittag = vormittag;
        this.nachmittag = nachmittag;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNacht() {
        return nacht;
    }

    public void setNacht(String nacht) {
        this.nacht = nacht;
    }
    public LocalDate getDatum() {
        return datum;
    }

    public void setDatum(LocalDate datum) {
        this.datum = datum;
    }
    public String getVormittag() {
        return vormittag;
    }

    public void setVormittag(String vormittag) {
        this.vormittag = vormittag;
    }
    public String getNachmittag() {
        return nachmittag;
    }

    public void setNachmittag(String nachmittag) {
        this.nachmittag = nachmittag;
    }

    public zlvp_Lager getZlvp_lager() {
        return zlvp_lager;
    }

    public void setZlvp_lager(zlvp_Lager zlvp_lager) {
        this.zlvp_lager = zlvp_lager;
    }

}