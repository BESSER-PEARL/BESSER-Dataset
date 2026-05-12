




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_bo_PanierBO  {

    private None listLivres;
    private int idPanier;
    private LocalDate date;
    private int quantity;



    public be_jebouquine_bo_PanierBO(
        None listLivres,        int idPanier,        LocalDate date,        int quantity    ) {
        this.listLivres = listLivres;
        this.idPanier = idPanier;
        this.date = date;
        this.quantity = quantity;
    }


    public None getListlivres() {
        return listLivres;
    }

    public void setListlivres(None listLivres) {
        this.listLivres = listLivres;
    }
    public int getIdpanier() {
        return idPanier;
    }

    public void setIdpanier(int idPanier) {
        this.idPanier = idPanier;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}