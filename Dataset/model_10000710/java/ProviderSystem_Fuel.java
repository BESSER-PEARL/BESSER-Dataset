




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ProviderSystem_Fuel  {

    private LocalDate date;
    private None plane;
    private int _price;
    private int volme;



    public ProviderSystem_Fuel(
        LocalDate date,        None plane,        int _price,        int volme    ) {
        this.date = date;
        this.plane = plane;
        this._price = _price;
        this.volme = volme;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public None getPlane() {
        return plane;
    }

    public void setPlane(None plane) {
        this.plane = plane;
    }
    public int get_price() {
        return _price;
    }

    public void set_price(int _price) {
        this._price = _price;
    }
    public int getVolme() {
        return volme;
    }

    public void setVolme(int volme) {
        this.volme = volme;
    }


}