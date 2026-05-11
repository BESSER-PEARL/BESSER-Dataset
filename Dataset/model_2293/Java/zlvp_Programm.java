




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class zlvp_Programm  {

    private String nachmittag;
    private String nacht;
    private int id;
    private LocalDate datum;
    private String vormittag;





    private zlvp_Lager zlvp_lager;


    public zlvp_Programm(
        String nachmittag,        String nacht,        int id,        LocalDate datum,        String vormittag    ) {
        this.nachmittag = nachmittag;
        this.nacht = nacht;
        this.id = id;
        this.datum = datum;
        this.vormittag = vormittag;
    }


    public String getNachmittag() {
        return nachmittag;
    }

    public void setNachmittag(String nachmittag) {
        this.nachmittag = nachmittag;
    }
    public String getNacht() {
        return nacht;
    }

    public void setNacht(String nacht) {
        this.nacht = nacht;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

    public zlvp_Lager getZlvp_lager() {
        return zlvp_lager;
    }

    public void setZlvp_lager(zlvp_Lager zlvp_lager) {
        this.zlvp_lager = zlvp_lager;
    }

}